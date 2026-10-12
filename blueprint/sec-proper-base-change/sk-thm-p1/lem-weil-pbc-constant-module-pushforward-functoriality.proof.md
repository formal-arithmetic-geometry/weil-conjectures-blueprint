+++
kind = "proof"
of = "lem-weil-pbc-constant-module-pushforward-functoriality"
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-weil-pbc-inverse-image-composition", "lemma-constructible-pullback-constant"]
+++
For g:Y2 -> Y1 over X, take the inverse-image unit at the constant M-sheaf, followed by g_* of the canonical comparison g^* M_Y1 -> M_Y2. Push this map forward by f1 and compose with the canonical g_* f1_* composition comparison. This is exactly constantModulePushforwardMap. ([lemma-constructible-pullback-constant], [def-weil-pbc-direct-image], [def-weil-pbc-inverse-image]).

Under the constant-sheaf/global-sections adjunction, the canonical pullback comparison preserves the section with each value m. On etale U over X the resulting map is restriction along U times_X Y2 -> U times_X Y1. Restrictions along an identity are identities, and along a composite are the composites in reverse order. This holds on the constant presheaves and extends uniquely to their sheafifications. The pushforward comparison is the fibre-product pasting map, so the identity and composition equalities are the asserted ones. Equivalently, take mates under the inverse-image adjunction and use its unit and composition coherence; the uniqueness of the constant-sheaf comparison gives the same mates. ([lemma-constructible-pullback-constant], [def-weil-pbc-direct-image], [lem-weil-pbc-inverse-image-composition]).
