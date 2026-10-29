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
| Pency | bank-robbing pencil | Shaving Shot x3, Bag Swing, Pencil Drop | Bank Heist (money bags that land on Pency heal him) | Robber Beanie |
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
| Raggy | a burlap sack and a bad guy, lives in jail | Rock Toss, Sack Swing, Bag Over Head | Jailbreak | Jailbird Cap |
| Ian | an elephant, the heaviest fighter | Trumpet, Trunk Grab, Big Stomp | Stampede | Circus Plume |
| Gary | a sheep who is the mayor | Campaign Flyer, Wool Roll, Town Meeting | Mayor's Parade | Ribbon Top Hat |
| Jacc | a jackrabbit in a top hat, the fastest hopper with three jumps | Carrot Toss, Big Hop, Thump | Rabbit Stampede | Stovepipe Hat |
| Horseshoe Crab | a crab with a sneaker on all six feet, wide and hard to launch | Bubble Blast, Claw Grab, Shoe Stomp | Sneaker Storm | Flip-Flop Hat |
| Gigi | a monkey in a straitjacket who fights with feet, tail and head | Banana Peel, Tail Whip, Tantrum | Breakout | Banana Beanie |
| Foxy | a sly fox, the other big bad guy next to Kayden | Fox Fire, Pounce, Sly Trick (counter) | Night Hunt | Bandit Fedora |

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
| The Slammer | Raggy's home: jail, because he got caught. Bunk platforms, bars, a searchlight |
| Watering Hole | Ian's home: a pond with drifting log platforms |
| Town Hall | Gary's home: the steps of Town Hall with podium platforms and confetti |
| Hat Haven (Battlefield) | the original battlefield: a flat stage with two low platforms and one up top, nobody's home |
| Desert Hop | Jacc's home: a sunset desert with cactus platforms and a rolling tumbleweed |
| Tide Pool | Horseshoe Crab's home: a beach with rolling waves, shell platforms and a drifting raft |
| Jungle Gym | Gigi's home: rainforest vines, bananas and monkey-bar platforms, one bobs up and down |
| Foxy's Den | Foxy's home: a moonlit pine forest with log platforms and eyes glowing in the burrow |
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
- **Raggy**: Sack Swing is a huge wide whip, Bag Over Head pulls opponents in.
- **Ian**: heaviest fighter, armor on his smashes, Trumpet shoves everyone away, Trunk Grab pulls them in.
- **Gary**: wool softens every hit he takes by 15%.
- **Jacc**: three jumps and the fastest ground speed in the game.
- **Horseshoe Crab**: shell armor on smashes, takes 8% less damage, Claw Grab pulls the opponent in.
- **Gigi**: no hands, so every attack is a kick, tail whip or head bonk. Extra-long rolls.
- **Foxy**: bites chew shields twice as fast, hits from behind do 30% more, Sly Trick counters anyone who swings first.
- **Luke Lava**: every hit sets the opponent on fire for two seconds of extra damage. Lava and burning puddles can't hurt him. Magma Pool leaves a burning puddle under him.

Move names flash above the fighter when they come out, and every attack is acted out: jaws open on bites, legs swing on kicks, heads lunge on headbutts, the body thrusts on stabs, batons sweep on swings, with a wind-up and follow-through.

## Personalized visuals

Each fighter idles, runs, jumps, lands, dodges and shields in its own style: Spike taps a hoof and leans into his run, Noodles pumps a flex and sprays water, Pency swings the money bag and hops stiffly, Bootisaurus sways his tail and shakes the ground when he runs, Baggy sways like paper and sheds scraps, Snakey twirls his baton and slithers. Shields are a water bubble, a leather dome, a paper bag, a pink eraser, a horned bubble and a police badge.

## Rules

- Damage percent goes up, knockback goes up. Get launched past the edge of the screen and you lose a stock.
- Every 60 seconds one random fighter gets a Final Smash. Press Special (no direction) to unleash it. Lose a stock and it's gone.
- The hat button in the bottom-left puts a hat on everyone. Every fighter has their own hat. Every hat has bells.

## Ronnie-Mode!

Tap left, up, right, down quickly in a row (keys or joystick) during a fight. Time slows, the camera zooms in, your fighter ties on a red karate headband and runs through a chop, a front kick, a spinning high kick and a bow while "Ronnie-Mode!" pops up over their head, and the music switches to the Ronnie-Mode theme. Then the fight resumes with your fighter powered up for 20 seconds:

- **Attack button**: long-reach karate chops. Karate Chop, Rising Chop, Low Chop, Mega Chop (smash), Air Chop, Falling Chop.
- **Special button**: Flying Kick (neutral or side), Spinning Jump Kick (up, also your recovery), Dive Kick (down in the air), Sweep Kick (down on the ground).

The headband stays on while it lasts and a timer shows above your HUD panel. Afterwards there is a 15-second cooldown before you can trigger it again. Losing a stock ends it. The Ronnie-Mode theme is an original martial-arts disco tune made by `music/make-ronnie-mode.py`: four-on-the-floor drums, octave-bouncing bass, a plucked pentatonic lead, brass stabs, a gong and a "HA!".

## Music and sound

The background music is Ronnie's own tunes, played on piano, with no vocals. `music/make-piano.py` listened to his recordings in two-second windows, picked the major or minor chord that best matched the notes he was singing, laid down a soft bass note and a broken chord, and played his melody notes on top. The recordings with his voice are not in the game or this repo anymore. Track 1 (piano) plays on the menus. Track 2 is the fight track: the same piano plus a distorted electric guitar riff from `music/make-guitar.py`, which plays palm-muted power-chord chugs, an accent on every bar, a riff fill every other bar and a harmony stab every fourth bar, all following the same chord changes. During Ronnie-Mode the Ronnie-Mode theme takes over. The Music and Sound buttons in the top-right corner turn either off.

No sound on a phone? iPhone: the ring/silent switch mutes web games until music starts, so flip it to ring or just tap PLAY and the music will unlock the sound effects too. Android: the game uses the media volume, not the ringer, so press volume-up while the game is open.

## Online: two devices, two players

Tap **ONLINE (2 DEVICES)** on the title screen. Phones, laptops and desktops all work, in any mix; on a computer either set of keys controls your fighter.

1. One device taps **HOST A GAME** and gets a 4-letter code.
2. The other device taps **JOIN WITH A CODE** and types it.
3. Both players pick their own fighter. The host is Player 1, picks the stage and stocks, and taps FIGHT.

How it works: the phones connect directly to each other (WebRTC through PeerJS's free public signaling server, no game server). The host phone runs the match and streams a compact snapshot every frame (about 7 KB/s); the guest phone sends its button presses and draws what it receives. Works best on the same Wi-Fi. Phone-to-phone across two cellular networks sometimes can't connect because of carrier firewalls. Keep both phones awake: switching apps drops the game. Online play needs the hosted version (https://stevedalyrealty.github.io/Ronnie-Stuff/) or the installed app, not the raw file.

## Controls

Two people share one keyboard without touching: Player 1 only uses the left half, Player 2 only uses the right half. The HOW TO PLAY screen shows a color-coded keyboard map.

**Player 1 (left half):** left hand on W A S D (up, left, crouch, right) with Space to jump. Right hand on F attack, G special, H shield, T smash (R also works). Left Shift also shields.
**Player 2 (right half):** right hand on the arrow keys (↑ up, ↓ crouch) with Right Shift to jump (Enter also works). Left hand on `,` attack, `.` special, `/` shield, M smash. Numpad 1 / 2 / 3 / 0 / 4 are attack, special, shield, jump, smash if you have one.
**Phone:** left thumb joystick, right thumb A / B / JUMP / SHIELD. Only the JUMP button jumps. Start your thumb a little in from the screen edge so the phone's back-swipe doesn't grab it.

Smash attacks: hold a direction and press the Smash key (keep holding to charge). Flicking a direction plus Attack still works too. Up (W / ↑) only does up-attacks by default so you never jump by accident. If you'd rather jump with W / ↑, pick "Also W / ↑" under Jump key on the fighter select screen.

Hold a direction plus Attack for a tilt. Attack while running for a dash attack. Shield plus a direction rolls. Shield in the air is an air dodge. Fall near an edge to grab the ledge. Esc pauses.
