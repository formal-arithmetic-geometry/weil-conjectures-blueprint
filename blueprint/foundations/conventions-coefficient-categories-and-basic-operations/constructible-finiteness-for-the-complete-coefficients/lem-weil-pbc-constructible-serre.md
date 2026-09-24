+++
id = "lem-weil-pbc-constructible-serre"
kind = "lemma"
title = "Constructible sheaves form a weak Serre subcategory"
order = 1336
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-etale-site", "lem-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
For a scheme $T$ and a finite ring $\Lambda$, the constructible
$\Lambda$-module sheaves on $T_{\Et}$ form a weak Serre subcategory of
$\Mod(T_{\Et},\Lambda)$: kernels, cokernels, and extensions of constructible
sheaves are constructible.

*Source:* Stacks Project, Etale Cohomology, Lemma 59.71.6, [Tag
03RZ](https://stacks.math.columbia.edu/tag/03RZ). The pro-etale counterpart
of the weak-Serre assertion, stated there for a Noetherian coefficient ring,
is Stacks Project, Section 61.27, [Tag
09AI](https://stacks.math.columbia.edu/tag/09AI); the form used here is the
etale statement just cited, for a finite ring $\Lambda$.

## Proof

Work on an affine open of $T$, and refine the finitely many partitions of
the given constructible sheaves to one common partition, as in the
definition of a constructible complex. Inverse image to a part is exact, by
the stalkwise exactness of geometric stalks. It suffices to prove the
assertions for finite locally constant sheaves on each part, locally for the
topology of the small etale site.

For a map between two such sheaves, trivialize both near a geometric point.
The images of the finitely many elements of the first constant module are
sections of the second. After an etale refinement each is a specified
constant section. The map is then induced by a map of finite modules, whose
kernel and cokernel give the constant kernel and cokernel sheaves. These
descriptions prove the first two assertions.

Consider an extension $0\to F'\to F\to F''\to0$ with $F'$ and $F''$ finite
locally constant. Fix a geometric point $\bar t$ and trivialize both outer
sheaves on an etale neighbourhood. By the exactness of geometric stalks, the
middle stalk $B=F_{\bar t}$ is an extension of two finite modules and is
finite. Represent each of its finitely many elements by a section of $F$ on
a common pointed etale neighbourhood. All addition, zero and
scalar-multiplication relations of $B$ hold after a further common
refinement: there are only finitely many relations since $B$ and $\Lambda$
are finite, and equality in a stalk means equality on such a neighbourhood.
Also impose the finitely many equalities identifying the chosen sections of
the submodule with the constant sections of $F'$, and their images with the
constant sections of $F''$. We obtain a map from the constant exact sequence
of stalk modules to the given exact sequence, which is the identity on the
outer terms. The kernel--cokernel argument for a map of short exact
sequences makes the middle map an isomorphism; equivalently, apply the same
argument on every stalk and conservativity of geometric stalks. Thus $F$ is
finite locally constant near every point. Applying this on the common
partition proves extension closure and completes the proof.
