+++
id = "prop-weil-pbc-normalization-comparison"
kind = "theorem"
title = "Normalization comparison"
order = 1617
tags = ["latex:proposition"]
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-extension-by-zero", "def-weil-pbc-finite-pushforward-extension-zero", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-direct-image-exact", "prop-weil-pbc-finite-pushforward-extension-zero-commute", "thm-weil-pbc-smooth-curve-calculations"]
+++
Let $C$ be a reduced curve, let $\nu:\widetilde C\to C$ be its finite
normalization, and let $j:U\hookrightarrow C$ be open. There is a natural
exact sequence

$$
 0\to j_!\mathbf F_r\longrightarrow
 \nu_*\widetilde j_!\mathbf F_r\longrightarrow Q\to0,
$$

where $Q$ is constructible and supported on the finite nonnormal locus. The
sequence, its boundary maps, and its restriction to opens commute with
algebraically closed field extension.

## Proof

The normalization $\nu:\widetilde C\to C$ is a finite morphism, hence has
exact direct image by [lem-weil-pbc-finite-direct-image-exact], and $\nu$ is
an isomorphism over the normal locus so that $\widetilde C\to C$ is an
isomorphism over the open part of the extension by zero
[def-weil-pbc-extension-by-zero] outside the finite nonnormal locus. The map
$j_!\mathbf F_r\to\nu_*\widetilde j_!\mathbf F_r$ is the diagonal finite-fibre
map: at a geometric point $\bar c\in U$ the target stalk is the product of
$\mathbf F_r$ over the finite geometric fibre of the normalization, computed
with the finite stalk formula, and the map is the adjoint of the unit; it is
injective with cokernel $Q$ supported on the finite nonnormal locus, and
exactness of the sequence follows from exactness of the two direct images and
the stalkwise computation. The cokernel $Q$ is constructible: it is the finite
pushforward of a constructible sheaf on the normal locus of the finite set of
nonnormal points. Naturality of the sequence in the algebraically closed
extension: the compatibilities of
[prop-weil-pbc-finite-pushforward-extension-zero-commute] (with the datum of
[def-weil-pbc-finite-pushforward-extension-zero]) and of the finite direct
image under pullback along $C_{k'}\to C$ transport the construction, and the
constant-sheaf invariance supplied by
[thm-weil-pbc-smooth-curve-calculations] makes the boundary maps and the
restrictions to opens compatible with *field extension*.
