few_shots = [
    {
        'Question'  :'which country has maximum co2 emission in the year of 2002',
        'SQLQuery'  :'SELECT Country_name FROM country_emissions WHERE `2002` = (SELECT MAX(`2002`) as max_value FROM country_emissions);',
        'SQLResult' :'Result of the SQL query',
        'Answer'    :'Qatar'
    },
    {
        'Question'  :'Which country had the maximum CO2 emissions in the year 2002, and to which income group category do they belong?',
        'SQLQuery'  :'SELECT ce.Country_name, ct.IncomeGroup FROM country_emissions AS ce JOIN country_table AS ct ON ce.Country_code = ct.Country_Code ORDER BY ce.`2002` DESC LIMIT 1;',
        'SQLResult' :'Result of the SQL query',
        'Answer'    :'Qatar, High income',
    },
    {
        'Question'  :'how many countries emit co2 in the range of 4.25 to 20 in the year of 2010',
        'SQLQuery'  :'SELECT COUNT(ce.Country_code) FROM country_emissions AS ce WHERE ce.`2010` BETWEEN 4.25 AND 20;',
        'SQLResult' :'Result of the SQL query',
        'Answer'    :'84',
    },
    {
        'Question'  :'No of countries emit co2 in the range of 1.25 to 15 in the year of 2010 AND 1990',
        'SQLQuery'  :'SELECT COUNT(country_name) AS country_count FROM country_emissions WHERE (`2010` BETWEEN 1.25 AND 15) AND (`1990` BETWEEN 1.25 AND 15);',
        'SQLResult' :'Result of the SQL query',
        'Answer'    :'119',
    },
    {
        'Question'  : 'Identify the number of countries that exceeded 2 standard deviations in 2013',
        'SQLQuery'  : 'SELECT COUNT(Country_name) FROM country_emissions JOIN (SELECT AVG(`1990`) + 2 * STDDEV(`1990`) AS upper_limit, AVG(`1990`) - 2 * STDDEV(`1990`) AS lower_limit FROM country_emissions) AS std ON country_emissions.`1990` < std.lower_limit OR country_emissions.`1990` > std.upper_limit;',
        'SQLResult' : 'Result of the SQL query',
        'Answer'    : '11', 
    },
    {
        'Question'  : 'Identify the countries that exceeded 2 standard deviations in 2013',
        'SQLQuery'  : 'SELECT Country_name FROM country_emissions JOIN (SELECT AVG(`2013`) + 2 * STDDEV(`2013`) AS upper_limit_2013, AVG(`2013`) - 2 * STDDEV(`2013`) AS lower_limit_2013, AVG(`2015`) + 2 * STDDEV(`2015`) AS upper_limit_2015, AVG(`2015`) - 2 * STDDEV(`2015`) AS lower_limit_2015 FROM country_emissions) AS std ON (country_emissions.`2013` < std.lower_limit_2013 OR country_emissions.`2013` > std.upper_limit_2013) AND(country_emissions.`2015` < std.lower_limit_2015 OR country_emissions.`2015` > std.upper_limit_2015);',
        'SQLResult' : 'Result of the SQL query',
        'Answer'    : 'Australia, Bahrain, Brunei Darussalam, Canada, Estonia, Kazakhstan, Kuwait, Luxembourg, Oman, Qatar, Saudi Arabia, Trinidad and Tobago, United Arab Emirates, United States', 
    },
    {
        'Question'  : 'Identify the total countries that exceeded 2 standard deviations in 2013 and 2015',
        'SQLQuery'  : 'SELECT COUNT(Country_name) FROM country_emissions JOIN (SELECT AVG(`2013`) + 2 * STDDEV(`2013`) AS upper_limit_2013, AVG(`2013`) - 2 * STDDEV(`2013`) AS lower_limit_2013, AVG(`2015`) + 2 * STDDEV(`2015`) AS upper_limit_2015, AVG(`2015`) - 2 * STDDEV(`2015`) AS lower_limit_2015 FROM country_emissions) AS std ON (country_emissions.`2013` < std.lower_limit_2013 OR country_emissions.`2013` > std.upper_limit_2013) AND(country_emissions.`2015` < std.lower_limit_2015 OR country_emissions.`2015` > std.upper_limit_2015);',
        'SQLResult' : 'Result of the SQL query',
        'Answer'    : '13', 
    },
    {
        'Question'  : 'Which country recorded the highest CO2 emissions in 2020,and what its emission value',
        'SQLQuery'  : 'SELECT Country_name, `2020` FROM country_emissions ORDER BY `2020` DESC LIMIT 1;',
        'SQLResult' : 'Result of the SQL query',
        'Answer'    : 'Qatar, 31.7268', 
    },

]