import CheatSheet from './generic/CheatSheet.jsx'

export default function Sets() {
  const rows = [
    {
      description: 'Declaration',
      javascript: [["const myFriends = new Set(['Ros', 'Fe', 'Ros'])"]],
      python: [["my_friends = {'Ros', 'Fe', 'Ros'}"]],
    },
    {
      description: 'Intersection',
      javascript: [['myFriends.intersection(yourFriends)']],
      python: [['my_friends.intersection(your_friends)', 'my_friends & your_friends']],
    },
    {
      description: 'Difference',
      javascript: [['myFriends.difference(yourFriends)']],
      python: [['my_friends.difference(your_friends)', 'my_friends - your_friends']],
    },
    {
      description: 'Union',
      javascript: [['myFriends.union(yourFriends)']],
      python: [['my_friends.union(your_friends)', 'my_friends | your_friends']],
    },
    {
      description: 'Symmetric Difference',
      javascript: [['myFriends.symmetricDifference(yourFriends)']],
      python: [['my_friends.symmetric_difference(your_friends)', 'my_friends ^ your_friends']],
    },
    {
      description: 'Empty a Set',
      javascript: [['myFriends.clear()', 'myFriends = new Set([])']],
      python: [['my_friends = set()']],
    },
  ]

  return (
    <CheatSheet
      title="Sets"
      intro="A collection of unique values."
      rows={rows}
    />
  )
}
