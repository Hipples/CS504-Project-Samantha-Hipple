report = "initial_pylint_tictactoe_results.txt"

class LintSorter:
    
    def __init__(self, lint):
        self.lint = lint

    def all_messages(self):
        msg_list = []
        with open(self.lint, 'r') as pylint:
            results = pylint.readlines()
        for msg in results:
            # print(msg)
            msg_list.append(msg.rstrip())
        return (msg_list)

    def message_type(self, type):
        msg_list = self.all_messages()
        sorted_report = "sorted_pylint_tictactoe_results.txt"
        with open(sorted_report, 'a+') as report:
            report.write('\n')
            for msg in msg_list:
                if type in msg:
                    print(msg)
                    report.write(msg)
                    report.write('\n')


select = LintSorter(report)
print()
select.message_type('C010') 
print()
select.message_type('C0114') 
print()
select.message_type('C0116') 
print()
select.message_type('C0301') 
print()
select.message_type('C0303') 
print()
select.message_type('C032') 
print()
select.message_type('C04')
print()
select.message_type('R0')
print()
select.message_type('R170')
print()
select.message_type('R1710')
print()
select.message_type('R1714')
print()
select.message_type('R172')
print()
select.message_type('W0')
print()
select.message_type('W13')
print()
select.message_type('W15')