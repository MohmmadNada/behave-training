# Training on Behave: 

### general Note to remember:
    1. the General command:  $ behave < file path > --no-capture
    2. run specific scenario : $ behave < file path > --n "scenario text"
    3. we can add arg. as "Admin" in feature.  and call it in step file "{user}" then send_keys(user), or as outline with diff, <"username"> params.
    4. we can fail the test; asser False,"add message".
    5. we can  pass the test; assert True,"we can add text also".
    6. good practice to use try: and except:.
    7. to execute number of steps before each scenario, use background. # behave-training
