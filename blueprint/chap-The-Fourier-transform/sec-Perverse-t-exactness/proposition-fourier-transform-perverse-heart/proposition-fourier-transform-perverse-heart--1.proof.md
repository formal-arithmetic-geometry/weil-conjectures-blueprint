+++
kind = "proof"
of = "proposition-fourier-transform-perverse-heart--1"
order = 1260004
uses = ["proposition-fourier-inversion", "lemma-artin-schreier-character-sheaf", "proposition-base-change-fourier-inversion", "lemma-finite-quasi-finite-direct-images"]
+++
Write $F=\operatorname{FT}_\psi$. Ordinary truncation gives a
distinguished triangle

$$
K_1\longrightarrow K\longrightarrow K_3\longrightarrow K_1[1],
\qquad K_1\in D^{\le n-1},\qquad
K_3\simeq\mathcal H^nK[-n].
$$

The transform is triangulated. Its upper amplitude bound gives
$F(K_1)\in D^{\le n}$, and $\mathcal H^nF(K_1)$ has finite support.
The first assertion follows by adjunction from Fourier inversion:
the inverse transform carries $D^{\ge a}$ into $D^{\ge a-1}$, so
$\operatorname{Hom}(F(K_1),Z)=0$ for $Z\in D^{\ge n+1}$.
Also, a sheaf of finite support transforms into a lisse sheaf shifted
by one. Thus $F(K_3)\in D^{\le n-1}$. The cohomology sequence of the
transformed triangle gives epimorphisms
$\mathcal H^aF(K_1)\to\mathcal H^aF(K)$ for $a\ge n$. They imply
the required vanishing for $a>n$ and finite support for $a=n$.

Here is the finite-support argument used in
`AlgebraicGeometry.support_homologySheaf_fourierTransform_finite`.
For $L\in D^{\le m}$, put $H=\mathcal H^{m+1}F(L)$ and
$N=\mathcal H^m(L(-1))$. A closed point $x$ in the support of $H$
gives a nonzero map $H\to i_*i^*H$, where $i$ is the closed immersion
of that point. Compose with the top truncation map of $F(L)$ and
apply $\operatorname{FT}_{\psi^{-1}}$. Fourier inversion and the
transform of a punctual sheaf give a nonzero map $N\to B$, where
$B$ is lisse and is geometrically a sum of linear character sheaves.
Its restriction to a dense open on which $N$ is lisse remains nonzero:
otherwise its image would have finite support, whose transform lies
in $D^{\le-1}$, whereas the transform of $B$ lies in $D^{\ge1}$.

After passing to the geometric fibre of this open, some component is
a nonzero map to $\mathcal L_{\psi(at)}$, where $-a$ is the coordinate
of a geometric point above $x$. Distinct closed points give distinct
parameters. The corresponding rank-one local systems are pairwise
nonisomorphic: tensoring a putative isomorphism with the inverse
character would make a nonzero linear character constant, contrary to
its ramification at infinity. A lisse sheaf of rank $r$ admits nonzero
maps to at most $r$ pairwise nonisomorphic irreducible local systems.
Consequently $H$ has finite support. This argument uses Fourier
inversion and character quotients in place of the formula for
$H_c^2$ in the human proof.

Finally apply the result for $\psi^{-1}$. By
Proposition [proposition-fourier-inversion], the quasi-inverse is
$\operatorname{FT}_{\psi^{-1}}(-)(1)$, and a Tate twist changes neither
vanishing nor support of the cohomology sheaves. It therefore preserves
the same upper classes.
