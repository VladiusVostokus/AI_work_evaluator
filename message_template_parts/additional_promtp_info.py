test_case_format = '''Functional Tests

Test 1.1 Traffic analysis over 1 minute

Test objective:

Setup Description:

Requirements:

===TABLE START===
|  | Steps | Expected result |
| --- | --- | --- |
| 1. |  |  |
| 2. |  |  |
| 3. |  |  |
| 4. |  |  |
===TABLE END===
'''

qa_requirements = '''3.2 Functional requirements

===TABLE START===
| ID | User requirements | Priority | User 
story 
link | Test 
link | BRD |
| --- | --- | --- | --- | --- | --- |
| FU-1 | Users must be able to capture network traffic in .pcap format during 1 minute. Capturing process should be started manually by running the script. | 1 | U-1 | T-1 
T-2 
T-3 | B-1 |
| FU-2 | Network data should be obtained via TFTP     protocol from a device using an ethernet 
connection to the server. In case of reboot during the sniffing process, all data will be lost. | 1 | U-2 | T-4 | B-2 |
===TABLE END===

3.3 Operational requirements

===TABLE START===
| ID | Operational requirements | Priority | User 
story | Test 
link | BRD |
| --- | --- | --- | --- | --- | --- |
| OR-1 | Software updates must be able to perform via tftpboot to eMMC. If process will be 
interrupted system should be able to recover from sdcard | 1 | U-3 | T-5 
T-6 | B-3 |
| OR-2 | Following item should be reflected in the serial log: 
● start and stop sniffing process 
● .pcap file is successfully transferred to the server | 2 | U-4 | T-7 
T-8 
T-9 | B4 |
| OR-3 | Version of software should be able to retrieve by command | 2 |  |  |  |
===TABLE END===

3.5 Non-functional requirements

===TABLE START===
| ID | Performance and stability | Priority | Test 
link | User 
Story | BRD |
| --- | --- | --- | --- | --- | --- |
| NFP-1 | Device should be able to capture data under Traffic load at least 50Mb/s | 1 | T-10 
T-11 |  |  |
| NFP-2 | System should be recovered after reboot via Power on/off. In case of reboot all captured data must be saved | 1 | T-12 |  |  |
===TABLE END===
'''