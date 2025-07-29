const gitHubUserRole = {
  name: "githubuser",
  alias: ["ghu"],
  doc: "Create a link to a user's GitHub profile",
  body: {
    type: String,
    doc: "The GitHub username, not inclusing an @",
    required: true,
  },
  run(data) {
    console.log(data);
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
    console.log(node);
    return [node];
  },
};

const plugin = {
  name: "GitHub",
  roles: [gitHubUserRole],
};

export default plugin;
