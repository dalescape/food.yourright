import csv
import json

snapcsv_file = 'SNAP-DATA.csv'
snapjson_file = 'snap_app/fixtures/snapdata.json'

snapdata = []

with open(snapcsv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        # Parse columns with list-like format
         # Remove square brackets from Sub-Program(s)
        sub_programs = row["Sub-Program(s)"].strip("['']")
        state_snap_program_name = row["State SNAP Program Name"][1:-1].strip("'").split(",")
    
        application_description_link = row["Application(s)"][1:-1].strip("''").split(",")  # Remove brackets and split into a list
        application_description = [item.strip("'").split(":")[0] for item in application_description_link]
        application_link = [item.strip("'").split(":", 1)[1].strip() for item in application_description_link]

                # Create a dictionary in the desired JSON format for each CSV row
        state_snap_program_json = {
            "model": "snap_app.StateSnapProgram",  # Add the "model" field
            "pk": None,  # Replace with the primary key if needed
            "fields": {
                "StateSNAPProgramName": state_snap_program_name,
            }
        }
        snapdata.append(state_snap_program_json)

        # Create a dictionary in the desired JSON format for each CSV row
        snap_data_json = {
            "model": "snap_app.SnapData",  # Add the "model" field
            "pk": None,  # Replace with the primary key if needed
            "fields": {
                "Organization": row["Organization"],
                "SubPrograms": sub_programs,  # Sub-Program(s) as a single string
                "SNAPWebsite": row["SNAP Website"],
                "StateEBTInfo": row["State EBT Info"],
            }
        }
        snapdata.append(snap_data_json)

        application_info_json = {
            "model": "snap_app.ApplicationInfo",  # Add the "model" field
            "pk": None,  # Replace with the primary key if needed
            "fields": {
                    "Description": [desc.strip().strip("'") for desc in application_description],  # Remove extra spaces
                    "Link": [link.strip() for link in application_link],  # Remove extra spaces
            }
        }
        snapdata.append(application_info_json)

        # Create many-to-many relationships
        snap_data_pk = len(snapdata) - 3
        state_snap_program_pk = len(snapdata) - 2
        application_info_pk = len(snapdata) - 1

        # Add relationships to SnapData
        snap_data_json["fields"]["state_snap_program_name"] = [state_snap_program_pk]
        snap_data_json["fields"]["applications"] = [application_info_pk]

        # Add relationships to StateSnapProgram
        state_snap_program_json["fields"]["snapdata"] = [snap_data_pk]

        # Add relationships to ApplicationInfo
        application_info_json["fields"]["snapdata"] = [snap_data_pk]
        application_info_json["fields"]["statesnapprogram"] = [state_snap_program_pk]


# Write the JSON data to the output file
with open(snapjson_file, 'w') as jsonfile:
    json.dump(snapdata, jsonfile, indent=4)