const gitHubUserRole = {
  name: "githubuser",
  alias: ["ghu"],
  doc: "Create a link to a GitHub profile",
  body: {
    type: String,
    doc: "The GitHub username, not inclusing an @",
    required: true,
  },
  run(data) {
    const node = {
      type: "link",
      url: `https://github.com/${data.body}`,
      children: [
        {
          type: "text",
          value: data.body,
        },
      ],
    };
    return [node];
  },
};

const orcidRole = {
  name: "orcid",
  doc: "Create a link to an ORCID profile",
  body: {
    type: String,
    doc: "The ORCID",
    required: true,
  },
  run(data) {
    const node = {
      type: "link",
      url: `https://orcid.org/${data.body}`,
      children: [
        {
          type: "text",
          value: data.body,
        },
      ],
    };
    return [node];
  },
};

const twitterRole = {
  name: "twitter",
  doc: "Create a link to a Twitter profile",
  body: {
    type: String,
    doc: "The Twitter profile name, not including an @",
    required: true,
  },
  run(data) {
    const node = {
      type: "link",
      url: `https://twitter.com/@${data.body}`,
      children: [
        {
          type: "text",
          value: "@" + data.body,
        },
      ],
    };
    return [node];
  },
}

const mastodonRole = {
  name: "mastodon",
  doc: "Create a link to a Mastodon profile",
  body: {
    type: String,
    doc: "The Mastodon profile and instance tag, without a leading @. For example username@mastodon.social",
    required: true,
  },
  run(data) {
    var items = data.body.split("@");
    var user = items[0];
    var instance = items[1];
    const node = {
      type: "link",
      url: `https://${instance}/@${user}`,
      children: [
        {
          type: "text",
          value: "@" + data.body,
        },
      ],
    };
    return [node];
  },
}

const plugin = {
  name: "Profile",
  roles: [
    gitHubUserRole,
    orcidRole,
    twitterRole,
    mastodonRole
  ],
};

export default plugin;
