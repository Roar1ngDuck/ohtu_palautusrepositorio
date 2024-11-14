*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Registration
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  kalle2
    Set Password  kalleABC
    Set Password Confirmation  kalleABC
    Submit Registration
    Register Should Fail With Message  Password must contain numbers of special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Registration
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Register Should Fail With Message  Username is already in use

Login After Successful Registration
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Logout
    Set Username  kalle2
    Set Password  kalle123
    Submit Login
    Login Should Succeed
    

Login After Failed Registration
    Set Username  kalle2
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Registration
    Go To Login Page
    Set Username  kalle2
    Set Password  kalle12
    Submit Login
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Logout
    Go To Main Page
    Click Button  Logout
