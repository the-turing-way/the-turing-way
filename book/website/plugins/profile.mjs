const gitHubUserRole = {
  name: "githubuser",
  alias: ["ghu"],
  doc: "Create a link to a GitHub profile",
  body: {
    type: String,
    doc: "The GitHub username, not including an @",
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
};

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
};

const websiteRole = {
  name: "website",
  doc: "Create a link to a personal website",
  body: {
    type: String,
    doc: "The website URL",
    required: true,
  },
  run(data) {
    // Strip http or https
    var name = data.body.replace(new RegExp("(http|https):\/\/", "g"), "");
    const node = {
      type: "link",
      url: data.body,
      children: [
        {
          type: "text",
          value: name,
        },
      ],
    };
    return [node];
  },
};

const communityRolesRole = {
  name: "communityroles",
  docs: "Create a list of your roles in the community",
  body: {
    type: String,
    doc: "A semicolon-separated (;) list of roles",
    required: true,
  },
  run(data) {
    const roles = data.body.split(";");
    let node = {};
    if (roles.length == 1) {
      node = {
        type: "text",
        value: roles[0],
      };
    } else {
      let items = [];
      for (const role of roles) {
        items.push({
          type: "listItem",
          spread: true,
          children: [{ type: "text", value: role }],
        });
      }
      node = {
        type: "list",
        ordered: false,
        spread: false,
        children: items,
      };
    }

    return [node];
  },
};

const profileDirective = {
  name: "profile",
  doc: "Build a user profile for our contributors record.",
  arg: {
    type: String,
    doc: "Your name",
    required: true,
  },
  // body: {},
  options: {
    bio: {
      type: String,
      doc: "A short biography.",
    },
    github: {
      type: String,
      doc: "Your GitHub username, not including an @",
    },
    highlights: {
      type: String,
      doc: "Your personal highlights from working in The Turing Way",
    },
    mastodon: {
      type: String,
      doc: "Your Mastodon profile and instance tag, without a leading @. For example username@mastodon.social",
    },
    more: {
      type: String,
      doc: "Any extra information you would like on your profile",
    },
    orcid: {
      type: String,
      doc: "Your ORCID",
    },
    quote: {
      type: String,
      doc: "A personal quote for your profile",
    },
    roles: {
      type: String,
      doc: "Your role(s), or previous role(s), in The Turing Way",
    },
    twitter: {
      type: String,
      doc: "The Twitter profile name, not including an @",
    },
    website: {
      type: String,
      docs: "Your personal website",
    },
  },
  run(data, vfile, ctx) {
    // Process options
    const bio = data.options?.bio ?? null;
    const github = data.options?.github ?? null;
    const highlights = data.options?.highlights ?? null;
    const mastodon = data.options?.mastodon ?? null;
    const more = data.options?.more ?? null;
    const orcid = data.options?.orcid ?? null;
    const quote = data.options?.quote ?? null;
    const roles = data.options?.roles ?? null;
    const twitter = data.options?.twitter ?? null;
    const website = data.options?.website ?? null;

    const name = data.arg;

    // Card children
    let card_children = [];

    // Profile name
    card_children.push({
      type: "cardTitle",
      children: [
        {
          type: "text",
          value: name,
        },
      ],
    });

    // List items
    let list_items = [];

    for (const [prefix, role, data] of [
      ["Role", communityRolesRole, roles],
      ["GitHub", gitHubUserRole, github],
      ["ORCID", orcidRole, orcid],
      ["Mastodon", mastodonRole, mastodon],
      ["Twitter", twitterRole, twitter],
      ["Website", websiteRole, website],
    ]) {
      if (data) {
        list_items.push(listItem(prefix, role, data));
      }
    }

    if (list_items.length != 0) {
      card_children.push({
        type: "list",
        ordered: false,
        spread: false,
        children: list_items,
      });
    }

    // Card items
    for (const [title, data] of [
      ["Short biography", bio],
      ["Personal higlights", highlights],
      ["More information", more],
    ]) {
      if (data) {
        // Parse data as MyST to allow Markdown formatting
        card_children.push(cardItem(title, ctx.parseMyst(data)));
      }
    }

    // Quote
    if (quote) {
      card_children.push({
        type: "blockquote",
        children: [
          {
            type: "paragraph",
            children: [{ type: "text", value: quote }],
          },
          {
            type: "paragraph",
            children: [{ type: "text", value: `-- ${name}` }],
          },
        ],
      });
    }

    // Create label from name
    const label = "profile-" + name.replaceAll(" ", "-").toLowerCase();

    // Create card
    let card = {
      type: "card",
      label: label,
      identifier: label,
      html_id: label,
      children: card_children,
    };

    let nodes = [];
    nodes.push({
      type: "block",
      children: [card],
    });

    return nodes;
  },
};

function listItem(prefix, role, data) {
  return {
    type: "listItem",
    spread: true,
    children: [
      {
        type: "text",
        value: `${prefix}: `,
      },
      role.run({ body: data })[0],
    ],
  };
}

function cardItem(title, nodes) {
  return {
    type: "card",
    children: [
      {
        type: "cardTitle",
        children: [{ type: "text", value: title }],
      },
      nodes,
    ],
  };
}

const plugin = {
  name: "Profile",
  directives: [profileDirective],
  roles: [
    gitHubUserRole,
    orcidRole,
    twitterRole,
    mastodonRole,
    websiteRole,
    communityRolesRole,
  ],
};

export default plugin;
