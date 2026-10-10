+++
id = "sec-fourier-transform"
kind = "section"
title = "Fourier Transform"
order = 2668
uses = ["sec-poincare-duality", "sec-smooth-purity", "sk-thm-av-final"]
+++
**Content.** For a vector bundle $V\to S$ of rank $r$ over $\mathbf F_q$ and
a nontrivial additive character $\psi$ ([sk-def-char]), the Artin–Schreier
sheaf $\mathcal L_\psi$ ([sk-def-as], [sk-lem-as-properties]) pulled back
along the duality pairing gives a lisse rank-one kernel $\mathcal K_\psi$ on
$V\times_SV^\vee$ ([sk-def-kernel], [sk-prop-kernel-lisse]), and the
Fourier–Deligne transform is
$\FT_\psi(K)=p_{2,!}(p_1^*K\otimes^L\mathcal K_\psi)[r]$ ([sk-def-ft]). The
section develops its weight-free properties from the six operations alone.
The stalk formula [sk-prop-stalk] turns every question into a fibre integral
$H^*_c(V_{\bar\xi},K\otimes\mathcal L_{\psi\langle x,\xi\rangle})[r]$; from it
come exactness, base change, base linearity and the exchange of
$\underline{E}$ and $\delta_0$. On the numerical side, the
Grothendieck–Lefschetz formula plus the trace of $\mathcal L_\psi$ gives the
Fourier trace formula, and orthogonality of characters then gives Plancherel.
On the functorial side, composing kernel transforms
([sk-lem-kernel-composition]) and computing the convolution
$\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi\cong\Delta_*\underline{E}(-r)[-2r]$
([sk-prop-convolution-kernel]) gives Fourier inversion.

**Key theorem.**

- Thm [sk-thm-inversion] (P13, Fourier inversion): for $V\cong\mathbf A^r$,
  $\FT_{\psi^{-1}}\FT_\psi(K)\cong K(-r)$ and
  $\FT_\psi\FT_\psi(K)\cong\iota'^*K(-r)$ functorially in $K$. Used in
  §[sec-deligne-laumon-a1].
- Thm [sk-thm-fourier-trace-formula] (P8, Fourier trace formula): on
  $\Aone$, $t_{\FT_\psi(K)}(y)=-\sum_{x\in\mathbf F_{q^n}}t_K(x)\,\psi(\Tr_{\mathbf F_{q^n}/\mathbf F_q}(xy))$.
  Used in §[sec-deligne-laumon-a1].
- Cor [sk-cor-plancherel] (P9, Plancherel):
  $\sum_{y}|\iota\,t_{\FT_\psi(K)}(y)|^2=q^n\sum_{x}|\iota\,t_K(x)|^2$ over
  $\mathbf F_{q^n}$. Used in §[sec-deligne-laumon-a1].
- Prop [sk-prop-stalk], [sk-prop-well-defined], [sk-prop-first-formula],
  [sk-prop-base-change], [sk-prop-base-linear] (P2–P5, P7, formal
  properties): $\FT_\psi$ is exact triangulated, has fibre-integral stalks,
  sends $\underline{E}\mapsto\delta_0(-1)[-1]$ and $\delta_0\mapsto\underline{E}[1]$,
  and commutes with base change and with tensoring by coefficients from the
  base. Used in §[sec-deligne-laumon-a1].

**References.**

- R. Kiehl and R. Weissauer, *Weil conjectures, perverse sheaves and
  $\ell$-adic Fourier transform* (statements of the section; the proofs
  follow the detailed Fourier–Deligne blueprint, with Laumon's normalization
  of the transform).
