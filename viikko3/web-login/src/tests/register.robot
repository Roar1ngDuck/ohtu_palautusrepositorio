*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle2
    Set Password  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  kalle12
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  kalle2
    Set Password  kalleABC
    Submit Credentials
    Register Should Fail With Message  Password must contain numbers of special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle2
    Set Passwords Explicitly  kalle123  kalle321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is already in use

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Set Passwords Explicitly
    [Arguments]  ${password}  ${password_confirmation}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password_confirmation}