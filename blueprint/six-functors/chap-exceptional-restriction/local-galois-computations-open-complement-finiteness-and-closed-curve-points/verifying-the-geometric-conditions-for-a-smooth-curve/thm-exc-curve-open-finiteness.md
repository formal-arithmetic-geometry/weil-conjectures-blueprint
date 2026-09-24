+++
id = "thm-exc-curve-open-finiteness"
kind = "theorem"
title = "Open-complement finiteness on a smooth curve"
order = 3326
uses = ["def-exc-continuous-cohomology", "def-sc-curves", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "lem-exc-dvr-galois", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-strict-henselization-stalk-formula", "thm-galois-fundamental"]
+++
Let $k$ be a finite field or its algebraic closure, let $T/k$
be a smooth curve, and let $Z$ be a
finite set of closed points, with
open complement
$j:U\hookrightarrow T$. Let $A$ be a finite ring killed by a
power of a prime $\ell\neq\operatorname{char}(k)$.
On the etale sites, direct image
satisfies

$$
R^qj_*M=0\quad(q>1)
$$

for every module sheaf $M$, and $R^qj_*F$ is
constructible
for every constructible sheaf $F$.

## Proof

At a geometric point over $U$, the functor $j^*j_*$ is the
identity and restriction is exact, so all positive direct-image stalks
are zero. At a geometric point $\bar z$ over $z\in Z$,
[prop-weil-pbc-strict-henselization-stalk-formula] gives

$$
(R^qj_*M)_{\bar z}=H^q(\operatorname{Spec}F_{\bar z},M|),
\quad F_{\bar z}=\operatorname{Frac}(\mathcal O^{\rm sh}_{T,\bar z}).
$$

Indeed, $T$ is regular by [lem-sc-smooth-regular], and
its one-dimensional closed-point local rings are discrete valuation
rings by [lem-sc-regular-dim1-dvr]. Strict henselization
preserves this property and excellence, and its residue field here
is algebraically closed. Removing the closed point from its spectrum
leaves exactly its fraction field.

On a field, etale module sheaves are discrete modules for the absolute
Galois group. Here is why the finite Galois dictionary suffices also
for arbitrary $M$: every finite set of elements of a discrete
module generates a finite stable submodule, and every sheaf is the
filtered union of its finite submodules on this field site.
The finite equivalence in [thm-galois-fundamental] therefore
extends to an exact equivalence of the whole module categories.
Sections are invariants, so their right derived functors are exactly
[def-exc-continuous-cohomology]. The vanishing assertion now
follows from [lem-exc-dvr-galois] and the conservative etale
stalks of [lemma-weil-pbc-geometric-stalk-conservative].

For a constructible $F$, its restriction to each fraction field
has finite module fibre. The same calculation makes the degree-zero
and degree-one stalks at every removed point finite. On $U$,
the degree-zero restriction is $F$, and the degree-one restriction
is zero. Use the finite stratification of $U$ for $F$, and add
the finitely many closed points in $Z$. On the spectrum of the
residue field of each such point, a finite continuous Galois module
is a locally constant finite sheaf. This partition therefore proves
constructibility in the precise sense of
[def-weil-pbc-constructible-complexes].
