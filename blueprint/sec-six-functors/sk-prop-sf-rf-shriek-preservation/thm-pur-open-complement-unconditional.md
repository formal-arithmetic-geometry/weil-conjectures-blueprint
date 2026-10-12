+++
id = "thm-pur-open-complement-unconditional"
kind = "theorem"
title = "The open-complement condition is unconditional and uniform in the coefficient ring"
order = 2420
uses = ["def-exc-direct-image-input", "def-exc-open-complement-bound", "def-pur-conventions", "def-sbc-affine-space", "def-weil-finite-field-fiber", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-exc-open-complement-known", "lem-kun-cd-sep-closed-point", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-strict-henselization-stalk-formula", "thm-dg-finite-type-constructibility", "thm-exc-curve-open-constructible-general", "thm-exc-curve-open-dimension-general", "thm-exc-direct-image-input-holds", "thm-pur-general-admissibility", "thm-sc-finite-type-torsion-cd"]
+++
Let $k$ be a separably closed field, let $A$ be a finite commutative ring
annihilated by a power of a prime $\ell\neq\operatorname{char}(k)$, let
$T$ be a finite-type
$k$-scheme of dimension at most $d$, and let
$j:V\hookrightarrow T$ be a
quasi-compact open immersion.
Then the pair $(V,T)$ satisfies the open-complement condition of
[def-exc-open-complement-bound] with $c=2d$, and it does so for
*every* finite coefficient ring $A$ of that shape at once: both
clauses hold — the vanishing $R^qj_*M=0$ for every $q>2d$ and every
sheaf $M$ of $A$-modules on $V_{\Et}$, and the
constructibility of
$R^qj_*F$ in every degree for every constructible $A$-sheaf $F$ — and
the constant $2d$ depends on $T$ alone, not on $A$. In particular, in
the setting of the global finite-field datum with $k=\Fbar$ and at the
finite coefficient stages $A=A_{E,n}$ of [def-pur-conventions], the
condition holds for every $n\geq1$ with the same constant $2d$; for the
chart complements $W_U\subseteq\mathbf A^{d_U}_V$ of the assembly
[thm-pur-general-admissibility], where
$d_U+\dim V\leq d_U+\dim Y$, it holds with
$c_U=2(d_U+\dim V)$, again independent of $n$.
