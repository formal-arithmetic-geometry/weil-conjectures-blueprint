+++
kind = "proof"
of = "lemma-artin-schreier-character-sheaf--1"
order = 1217009
uses = ["proposition-topos-functoriality"]
+++
After pullback along the finite étale cover $u^q-u=x$, the direct image
of the constant sheaf splits into copies indexed by $k_0$. The projector
$e_\psi$ factors as averaging followed by a splitting, whose image is a
single copy of $\Qbarl$. This proves lissity; pulling back along
$x\mapsto ax$ preserves it. A geometric point lifts through the cover,
so its stalk is a line, and stalk dimensions are preserved by pullback.
These are the arguments of
`AlgebraicGeometry.WeilSheaf.isLisse_image_artinSchreierIdempotent` and
`AlgebraicGeometry.WeilSheaf.finrank_stalkObj_image_artinSchreierIdempotent`.

Evaluation on the cover gives an isomorphism of Weil sheaves
$\operatorname{AS}^*\mathcal L_\psi\simeq\Qbarl$, constructed in
`AlgebraicGeometry.WeilSheaf.upperStarArtinSchreierMapImageIso`.
Since $\operatorname{AS}\circ[0]=[0]$, pullback along $[0]$ gives the
constant sheaf, by functoriality of pullback. This establishes the
zero-map assertion without a compatibility assertion for multiplication
or duality.
