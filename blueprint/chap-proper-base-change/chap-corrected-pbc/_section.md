+++
id = "chap-corrected-pbc"
kind = "section"
title = "Corrected typed finite-level interface"
order = 636
+++
**Status.** This chapter is the authoritative typing boundary for the ordinary finite-level proof. It replaces the ill-typed historical sectionwise S0 formula. Every named S0–S7 middle owner remains OPEN/INCOMPLETE, and every atomic input is listed in Appendix [app-gap-ledger].

For a Cartesian square of noetherian finite-dimensional schemes

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
\mathllap{f'}\downarrow&&\downarrow\mathrlap{f}\\
Y'&\xrightarrow{g}&Y,
\end{array}
$$

and $K\in D_c^+(X,\Lambda_n)$, first construct in the ambient category the
single derived morphism

$$
\begin{split}
\operatorname{BC}_{f,g,K}:Lg^*Rf_*K
&\xrightarrow{\eta_{f'}}Rf'_*Lf'^*Lg^*Rf_*K\\
&\xrightarrow{\mathrm{cart}}Rf'_*Lg'^*Lf^*Rf_*K
\xrightarrow{Rf'_*(Lg'^*\varepsilon_f)}Rf'_*Lg'^*K.
\end{split}
\tag{BA31-MATE}
$$

Replacement independence and naturality concern this fixed map. Its identity,
horizontal-pasting, and vertical-pasting equations must be proved by adjunction
and mate calculus.

Two stalk facts have disjoint types and disjoint uses:

1. `CAT-BA31-SHEAF-STALK-FAITHFULNESS`: if
$u,v:\mathcal F\to\mathcal G$ are maps in the abelian category of
$\Lambda_n$-sheaves and $u_{\bar y}=v_{\bar y}$ at every geometric
point, then $u=v$. It is consumed only in S5, after the maps of
cohomology sheaves have already been constructed.
1. `CAT-BA31-DERIVED-STALK-ISO-CONSERVATIVITY`: if
$u:A\to B$ is an already constructed morphism in
$D^+(Y'_{\acute et},\Lambda_n)$ and every
$H^i(u)_{\bar y}$ is invertible, then $u$ is invertible. It is consumed
only in S6.

No stalk principle in this fragment detects equality of arbitrary derived
morphisms or constructs a derived inverse from pointwise inverses.

**S0–S7 middle interfaces.**

The following are literal middle owners and all remain
`OPEN/INCOMPLETE`.

- `OBL-BA31-S0-GLOBAL-MATE` constructs (BA31-MATE) and
proves replacement independence, naturality, identity, and both pasting
laws from the three named categorical atoms.
- `OBL-BA31-S1-FINITE` proves exact finite pushforward and the
finite geometric-fibre product formula, then identifies the latter with
the stalk of the already constructed mate.
- `OBL-BA31-S2-STABILITY` proves typed composition and
proper-surjective cancellation diagrams for the actual $Rf_*$
pseudofunctor; no inverse is supplied as input data.
- `OBL-BA31-S3-PROJECTIVE-REDUCTION` states a proper finitely
presented Chow datum and a finite-surjective retract/cancellation theorem
reducing projective space to products of projective lines.
- `OBL-BA31-S4-HENSELIAN-P1` assembles independently owned
degree-zero, affine, and torsor/degree-one theorems into the strict-henselian
projective-line comparison.
- `OBL-BA31-S5-STALK-COMPARISON` combines the strict-henselization
stalk formula and proper-curve field invariance and identifies their
comparison with $H^i(\operatorname{BC}_{f,g,K})$. Sheaf-stalk
faithfulness is used only for this equality of maps of $H^i$-sheaves.
- `OBL-BA31-S6-SHEAF-ASSEMBLY` applies only derived-stalk
isomorphism conservativity to the fixed mate after S1–S5 have proved all
its cohomology-stalk maps invertible.
- `OBL-BA31-S7-BOUNDED-BELOW` uses the selected bounded-below
Postnikov/Cartan–Eilenberg leaf, including convergence and identification
of the filtered comparison with (BA31-MATE).

The root `OBL-BA31-FINITE-PBC` remains
`OPEN/INCOMPLETE` until these middle nodes and every listed atom are
actually proved. The historical finite stalk-descent certificate is retired
and has no edge into this graph.
