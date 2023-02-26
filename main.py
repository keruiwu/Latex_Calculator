from parsing import parsing
from limit import cal_limit
from derivative import derivative
from integral import integral
from gradiant import gradiant
from number import Decimal_convertB
from number import Binary_convertD
from Brick import Brick
from Unary_quadratic import Unary_quadratic
import pyperclip
from wox import Wox


class LatexCalculator(Wox):
    def copy_result(self, result):
        pyperclip.copy(result)

    def query(self, query: str):
        output_results = []
        if query[-2:] == '$$':
            # output_results.append({
            #     'Title': "check",
            #     'SubTitle': 'check', 
            #     "IcoPath": 'Images/icon.ico'
            # })
            li = str(query).split()
            li[1] = ''.join(li[1:])
            equation = parsing(li[1].replace('\\\\', '\\'))
            output_results.append({
                'Title': str(equation),
                'SubTitle': 'check', 
                "IcoPath": 'Images/icon.ico', 
                "JsonRPCAction": {
                    "method": "copy_result",
                    "parameters": [str(equation)], 
                    "dontHideAfterAction": False
                }
            })
            result = 'Empty'
            # if li[0] == '-l' or li[0] == '--limit':  # limit
            #     result = str(cal_limit(str(equation)))
            if li[0] == '-d' or li[0] == '--derivative':
                result = derivative(equation)
            # elif li[0] == '-i' or li[0] == '--integral':
            #     result = integral(equation)
            elif li[0] == '-g' or li[0] == '--gradient':
                result = gradiant(equation)
            elif li[0] == '-b' or li[0] == '--brick':
                result = Brick(equation)
            elif li[0] =='-q' or li[0] == '--quadratic':
                result_list = Unary_quadratic(equation)
                for i in result_list:
                    output_results.append({
                        'Title': str(i),
                        'SubTitle': 'yeah', 
                        "IcoPath": 'Images/icon.ico', 
                        "JsonRPCAction": {
                            "method": "copy_result",
                            "parameters": [str(i)], 
                            "dontHideAfterAction": False
                        }
                    })
                return output_results

            output_results.append({
                'Title': str(result),
                'SubTitle': 'yeah', 
                "IcoPath": 'Images/icon.ico',
                'JSONRPCAction': {
                    'method': 'copy_result',
                    'parameters': [str(result)],
                    'dontHideAfterAction': False
                }
            })
        elif query[0:2] == '0d' and len(query) > 2:  # 10 -> 2
            num = query[2:]
            result = Decimal_convertB(int(num))
            for x, y in zip(result['Title'], result['Subtitle']):
                output_results.append({
                    'Title': x,
                    'SubTitle': y,
                    "IcoPath": 'Images/icon.ico',
                    'JSONRPCAction': {
                        'method': 'copy_result',
                        'parameters': [result],
                        'dontHideAfterAction': False
                    }
                })
        elif query[0:2] == '0b' and len(query) > 2:  # 2 -> 10
            num = query[2:]
            binary = Binary_convertD(num)
            output_results.append({
                'Title': binary,
                "IcoPath": 'Images/icon.ico',
                'JSONRPCAction': {
                    'method': 'copy_result',
                    'parameters': [binary],
                    'dontHideAfterAction': False
                }
            })
        output_results.append({
            'Title': query,
            'SubTitle': 'first', 
            "IcoPath": 'Images/icon.ico'
        })
        return output_results





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    LatexCalculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
