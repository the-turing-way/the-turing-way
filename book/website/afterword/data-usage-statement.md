(data-usage)=
# TTW Book Data Usage

We want to collect data on the reach and findability of The Turing Way book.
For example, data on website traffic helps with reporting impact.
Data on search terms people use to find the  website can help us understand readers' needs and preferences. 
With this knowledge we can better tailor our content to be useful.

See our ongoing discussions around which insights could help improve the content quality [on GitHub](https://github.com/the-turing-way/the-turing-way/discussions/3713)

## User Awareness Statement - Google Analytics
For the above reasons reason, we are currently tracking website traffic data through Google Analytics.
But, Google Analytics is [problematic](https://piwik.pro/blog/is-google-analytics-gdpr-compliant/).
We are working on using an open-source, GDPR-compliant analytics tool like [Matomo](https://matomo.org/) instead.

For now, we configured Google Analytics to be as GDPR-compliant as possible:

- Our data retention settings are set to the minimum duration possible (2 months).
- All advertising features are disabled.
- We do not send user IDs to Google.
- We do not share any collected data with Google beyond what is required of us to ["maintain and protect the Google Analytics service."](https://business.safety.google/adsprocessorterms/)
- (IP addresses are now anonymized per default)

By implementing these measures, we hope to somewhat mitigate the adverse effects of Google Analytics while we transition to a better tool.

