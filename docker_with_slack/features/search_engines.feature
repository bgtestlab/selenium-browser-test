@engine
Feature: Search Engines
    Traverse search engines

    @sanity
    Scenario: Go to google engine
        Given I can see the google homepage
        When I enter the keyword 'hello' in the search box
        Then I should not see the error message

    @functional @expect-failure
    Scenario Outline: Go to search engines other than google
        Given I can see the search engine <website> homepage
        When I enter the keyword 'hello' in the search box
        Then I should not see the error message
        Examples:
            | website        |
            | naver.com      |
            | duckduckgo.com |