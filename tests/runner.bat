ECHO OFF
pytest %1 %2 %3 %4 -s --alluredir="../reports"
allure serve C:\Users\Partha\PycharmProjects\UIAutomation\reports