+++
kind  = "proof"
of    = "sk-cor-nagata-sketch-proper-extension"
uses = ["sk-lem-nagata-sketch-elimination", "sk-lem-nagata-boundary-divisor", "sk-lem-nagata-sketch-blowups", "sk-lem-nagata-sketch-closure"]
+++
Take the schematic closure $G$ of the graph of $a$ in $T\times_SY$
([sk-lem-nagata-sketch-closure]). The projection $G\to T$ is proper, since
$Y\to S$ is proper, and is an isomorphism over $U$. First make $U$
schematically dense by [sk-lem-nagata-boundary-divisor], and replace $G$ by
its strict transform. [sk-lem-nagata-sketch-elimination] then makes the
strict transform of $G$ an open subscheme of a further blow-up $T'$. It is
also proper over $T'$, being closed in the proper base change of $G$. Its
image is thus closed as well as open and contains the schematically dense
$U$. It is all of $T'$. The strict transform is therefore isomorphic to
$T'$, and its map to $Y$ is the desired extension.
[sk-lem-nagata-sketch-blowups] combines the successive modifications into a
single admissible blow-up.

(Equivalently, one may apply the partial-section extension
[thm-nagata-conrad-elimination] to the section of $Y\times_ST\to T$ over $U$.)
