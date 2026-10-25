# Super Hat Bros

A Smash-style platform fighter that runs in any browser. One file, no install.

## Install it as an app

The game is a Progressive Web App. Once the repo is published with GitHub Pages it lives at
https://stevedalyrealty.github.io/Ronnie-Stuff/ and installs like a normal app:

- **Android / Chrome / Edge:** open the link, tap the Install button on the title screen (or browser menu → Install app).
- **iPhone / iPad:** open the link in Safari, tap Share, then Add to Home Screen.
- **Windows / Mac:** open the link in Chrome or Edge, click the install icon in the address bar or the Install button on the title screen.

It gets its own icon, launches fullscreen, and works offline after the first load.

## Or just download the file

1. Download `Super-Hat-Bros.html`.
2. Double-click it (computer) or open it from your Files / Downloads app (phone).
3. On a phone, turn it sideways. A joystick and buttons appear when the fight starts.

Works offline. The only thing that needs internet is the fancy font.

## Files

- `index.html`, `manifest.webmanifest`, `sw.js`, `icons/`: the installable app. Drop this folder on any static host (GitHub Pages, Netlify, your own server) and it installs.
- `Super-Hat-Bros.html`: the single-file version.
- `.github/workflows/pages.yml`: deploys the app to GitHub Pages on every push to main.

## Fighters

| Fighter | Who | Signature | Final Smash | Hat |
|---|---|---|---|---|
| Spike | headbutting goat | Goat Ram, Horn Toss, Hoof Stomp | Mega Ram | Pirate Tricorn |
| Noodles | flexing orca | Breach, Spout, Belly Flop | Tidal Wave | Sailor Cap |
| Pency | bank-robbing pencil | Shaving Shot x3, Bag Swing, Pencil Drop | Bank Heist | Robber Beanie |
| Bootisaurus Rex | T. Rex made of boots, twice the size | Chomp, Lace Whip, Boot Stomp | Boot Quake | Spur Cowboy Hat |
| Baggy | a bag with no arms, four jumps | Bag of Tricks, Bag Roll, Puff Up | Trash Tornado | Nightcap |
| Snakey | snake police officer | Ticket Toss, Slither Charge, Coil Counter | Full Arrest | Siren Cap |
| Cloudy | a cloud with fists and no legs, hovers | Lightning Bolt, Gust, Rain Dance | Super Storm | Umbrella Hat |
| Franchesca | a fish with legs and eyelashes | Bubble Shot, Fish Flop, Splash Zone | School of Fish | Fishing Hat |
| Shoean | a shoe with a lace bow, fastest runner | Lace Shot, Lace Lasso, Spring Sole | Marathon Dash | Sock Beanie |
| Luke Lava | a blob of red-hot lava, no arms or legs | Fireball, Lava Flow, Magma Pool | Eruption | Volcano Cap |
| Kayden | a knife who is a ninja and a bad guy | Shuriken, Blade Dash, Smoke Bomb | Thousand Blades | Straw Kasa |
| Po-po | a bead who is a police cop | Donut Toss, Cuff Toss, Siren Spin | Riot Charge | Donut Hat |
| Larry | a giraffe with the longest reach | Neck Snap, Gallop, Leaf Shower | Tall Order | Pith Helmet |
| Rollo | a rolled-up rug and a bad guy, lives in jail | Dust Puff, Unroll, Wrap Up | Jailbreak | Jailbird Cap |
| Ian | an elephant, the heaviest fighter | Trumpet, Trunk Grab, Big Stomp | Stampede | Circus Plume |
| Gary | a sheep who is the mayor | Campaign Flyer, Wool Roll, Town Meeting | Mayor's Parade | Ribbon Top Hat |

Every fighter was drawn on paper first.

## Stages

| Stage | Twist |
|---|---|
| Goat Peak | snowy summit, two high side ledges |
| Orca Cove | a boat platform drifts back and forth |
| Pency's Vault | gold-bar platforms, the middle one rides up and down |
| Boot Canyon | Bootisaurus' home: the stage is a giant boot |
| Baggy's Dump | Baggy's home: tires roll back and forth as platforms |
| Snakey's Precinct | Snakey's home: squad cars patrol as platforms, lights flash |
| Cloud Nine | Cloudy's home: a cloud stage in the sky, side clouds drift, rainbow behind |
| Fish Tank | Franchesca's home: inside an aquarium, slow falls, seaweed platforms sway |
| Shoebox Stack | Shoean's home: a shoe store, shoebox platforms, the top one slides |
| Shadow Dojo | Kayden's home: a dojo at night with paper lantern platforms |
| Traffic Stop | Po-po's home: a highway at night, two cars drive past as platforms |
| Savanna Treetops | Larry's home: acacia branch platforms over a sunset |
| The Slammer | Rollo's home: jail, because he got caught. Bunk platforms, bars, a searchlight |
| Watering Hole | Ian's home: a pond with drifting log platforms |
| Town Hall | Gary's home: the steps of Town Hall with podium platforms and confetti |
| Lava Lift | Luke Lava's home and a hazard stage: side platforms ride up and down, lava rains from the volcano, burns on contact and leaves burning puddles. Luke is immune |

Pick Random on the select screen to shuffle.

## Signature mechanics

Every fighter has its own named normal attacks, its own reach and angles, and one trick nobody else has:

- **Spike**: smash attacks have armor. Weak hits do damage but never knock him out of the swing.
- **Noodles**: bites chew through shields at double speed. Chomp Chomp and Barrel Roll hit several times.
- **Pency**: tipper. Land the very point of a stab for bonus damage and launch, marked TIP!
- **Bootisaurus Rex**: heavy armor on smashes and Lace Whip. Ground attacks kick up dust.
- **Baggy**: Pogo Stomp bounces him back up off whoever it hits. Dropkick lunges, Rustle Spin multi-hits.
- **Snakey**: Baton Combo is a three-hit jab. Tail Trip pulls the opponent toward him for a follow-up.
- **Cloudy**: five jumps and a hover (hold JUMP in the air). Lightning moves crackle, Gust shoves opponents a long way.
- **Franchesca**: slippery. Rolls go half again as far. Flop moves flip her whole body over.
- **Shoean**: fastest runner. The longer the run-up before a Sprint Kick, the harder it hits (SPRINT!). Lace Lasso pulls opponents in.
- **Kayden**: hits from behind do 30% more. Rolls are shadow steps. Smoke Bomb makes him near-invisible for a moment.
- **Po-po**: bounces back up when he lands hard. Cuff Toss pulls opponents in.
- **Larry**: the longest reach in the game, especially straight up.
- **Rollo**: Unroll is a huge flat whip, Wrap Up pulls opponents in.
- **Ian**: heaviest fighter, armor on his smashes, Trumpet shoves everyone away, Trunk Grab pulls them in.
- **Gary**: wool softens every hit he takes by 15%.
- **Luke Lava**: every hit sets the opponent on fire for two seconds of extra damage. Lava and burning puddles can't hurt him. Magma Pool leaves a burning puddle under him.

Move names flash above the fighter when they come out, and every attack is acted out: jaws open on bites, legs swing on kicks, heads lunge on headbutts, the body thrusts on stabs, batons sweep on swings, with a wind-up and follow-through.

## Personalized visuals

Each fighter idles, runs, jumps, lands, dodges and shields in its own style: Spike taps a hoof and leans into his run, Noodles pumps a flex and sprays water, Pency swings the money bag and hops stiffly, Bootisaurus sways his tail and shakes the ground when he runs, Baggy sways like paper and sheds scraps, Snakey twirls his baton and slithers. Shields are a water bubble, a leather dome, a paper bag, a pink eraser, a horned bubble and a police badge.

## Rules

- Damage percent goes up, knockback goes up. Get launched past the edge of the screen and you lose a stock.
- Every 60 seconds one random fighter gets a Final Smash. Press Special (no direction) to unleash it. Lose a stock and it's gone.
- The hat button in the bottom-left puts a hat on everyone. Every fighter has their own hat. Every hat has bells.

## Controls

**Player 1:** A / D move, W or Space jump, S crouch or fast fall, J attack, K special, L or Shift shield.
**Player 2:** Arrow keys, `,` attack, `.` special, `/` shield (or Numpad 1 2 3, Numpad 0 jump).
**Phone:** left thumb joystick, right thumb A / B / JUMP / SHIELD. Only the JUMP button jumps. Start your thumb a little in from the screen edge so the phone's back-swipe doesn't grab it.

Flick a direction and attack at the same time for a smash attack (hold to charge). Shield plus a direction rolls. Shield in the air is an air dodge. Fall near an edge to grab the ledge. Esc pauses.
