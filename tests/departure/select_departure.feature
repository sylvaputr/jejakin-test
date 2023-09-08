Feature: Verifying user case search departure and arrival location

        Scenario: The modal departure option will show
            Given Open Browser
             Then Click on edit icon
             Then the modal departure should be appear
             Then Input Soekarno Hatta on departure input field
             Then Click Soekarno Hatta departure
             Then Input Ngurah on arrival input field
             Then Click Ngurah arrival
             Then Click the pencil icon in the upper right corner next to passenger to add passengers
             Then Choose the cabin class
             Then Choose the number of passengers
             Then Click save button passenger
             Then Click the pencil icon in the upper right corner next to travel purpose to add travel purpose
             Then Choose the travel purpose
             Then Click the Take Action button
             Then Choose one of the programs to participate in
             Then Click the pencil button
             Then Input amount to contribute
             Then Click save button
             Then Input name on fullname input
             Then Input email on email input
             Then Click select payment method
             Then Choose one payment method
             Then Click I agree with the Terms & Conditions
             Then Click pay and offset
