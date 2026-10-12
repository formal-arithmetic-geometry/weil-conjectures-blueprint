+++
id = "sec-deligne-laumon-a1"
kind = "section"
title = "Deligne–Laumon on the Affine Line: Proof Sketch"
order = 3025
uses = ["sec-algebraic-groups-lie-algebras", "sec-fourier-transform", "sec-poincare-duality", "sec-purity-real-sheaves", "sec-six-functors", "sec-smooth-purity", "sec-trace-formula"]
+++
**Content.** Let $j\colon U_0\hookrightarrow\mathbf A^1_{\mathbf F_q}$ be a
dense open and $F$ a lisse Weil sheaf on $U_0$, pure of weight $w$ and
unramified at infinity. This section proves that $H_c^r(\mathbf A^1,j_*F)$
has weights at most $w+r$. Degrees $0$ and $2$ are elementary
[sk-l-dl-a1-endpoints], so the work is in degree one. For an irreducible
sheaf $M$ that is not geometrically constant, the Fourier transform is
exact on curve perverse sheaves [sk-p-dl-a1-perverse]. It sends
$(j_*M)[1]$ to a middle extension $(j'_*M')[1]$ [sk-p-dl-a1-middle], whose
stalk at $0$ is $H_c^1(\mathbf A^1,j_*M)$. A real envelope built from
$j_!M$ shows that $M'$ is pure of some weight $v$
[sk-p-dl-a1-some-weight]. Plancherel then bounds the trace energy of $M'$,
and the positivity argument of [sk-l-dl-a1-energy] gives $v\le w+1$
[sk-p-dl-a1-fourier-weight], [sk-c-dl-a1-hc1]. Finally, middle extension
is exact at a fixed pure weight [sk-p-dl-a1-exact], so the bound passes
through a composition filtration of $F$ [sk-thm-dl-a1-upper].

**Key theorem.**

- Thm [sk-thm-dl-a1-upper] (Deligne–Laumon affine-line estimate): for $F$
  lisse on a dense open $U_0\subset\mathbf A^1_{\mathbf F_q}$, pure of
  weight $w$ and unramified at infinity, $H_c^r(\mathbf A^1,j_*F)$ has
  weights at most $w+r$ for every $r$. Used in §[sec-deligne-laumon-general],
  §[sec-zeta-weil].
- Lemma [sk-l-dl-a1-energy] (weight detection by trace energy): if
  $N\ne0$ is lisse and pure of weight $v$ on an affine curve and
  $\sum_{x}|\iota\operatorname{Tr}(\mathrm{Frob}_x\mid N_{\bar x})|^2\le Cq^{nB}$
  for all $n$, then $v\le B-1$. Used in §[sec-deligne-laumon-general].

**References.**

- R. Kiehl and R. Weissauer, *Weil Conjectures, Perverse Sheaves and
  $\ell$-adic Fourier Transform* (the section follows its Deligne–Laumon
  argument for the affine line).
