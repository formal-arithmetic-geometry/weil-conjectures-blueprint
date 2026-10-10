+++
id = "sec-trace-formula"
kind = "section"
title = "Trace Formula"
order = 2265
uses = ["sec-curve-estimates", "sec-six-functors", "sec-smooth-purity"]
+++
**Content.** For a Weil complex $(K,\varphi)$ on a separated finite-type
$X_0/\mathbf F_q$ this section proves the Grothendieck–Lefschetz trace
formula: the trace of Frobenius on $R\Gamma_c(X,K)$ equals the sum of stalk
traces over $X_0(\mathbf F_{q^m})$. The route is Lefschetz–Verdier. From the
six operations one builds trace classes of cohomological correspondences
and the supported pairing [sk-p-pairing], proves compatibility with proper
pushforward [sk-p-proper], and deduces that on a proper $X$ the global trace
is the integral of the trace class over the fixed locus
[sk-c-proper-global]. When the fixed locus is a finite union of clopen
pieces, that integral splits into local terms [sk-p-local]. On a smooth
curve the Frobenius graph is contracting, so each local term is the naive
stalk trace [sk-p-frob]. The formula on $\mathbf P^1$ gives it for closed
subschemes of $\mathbf A^1$. Induction on the number of coordinates via
$!$-pushforward and compact trace additivity extends it to all schemes
[sk-thm-trace-formula]. Compatibility with coefficient reduction and adic
realization [sk-prop-trace-adic] carry it to $\mathcal O_E$, $E$ and
$\overline{\mathbf Q}_\ell$, and the logarithm of the Frobenius determinant
[sk-prop-logdet] turns it into the Euler-product identity for $L$-functions
[sk-thm-trace-transport].

**Key theorem.**

- Prop [sk-thm-trace-formula] (finite-coefficient Lefschetz trace formula):
  for a Weil datum $K\in D^b_{ctf}(X,A)$ and every $m\ge1$,
  $\tr_A(F_{c,m}\mid R\Gamma_c(X,K))=\sum_{x\in X_0(\mathbf F_{q^m})}\tr_A(F_{x,m}\mid K_{\bar x})$.
  Used in §[sec-zeta-weil].
- Thm [sk-thm-trace-transport] (trace formula at the non-finite stages): the
  same identity holds with coefficients in $\mathcal O_E$, $E$,
  $\overline{\mathbf Q}_\ell$. Over the fields it is equivalent to
  $L(X_0,K,T)=\prod_i\det(1-TF\mid H^i_c(X,K))^{(-1)^{i+1}}$. Used in
  §[sec-purity-real-sheaves], §[sec-fourier-transform],
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general],
  §[sec-zeta-weil].
- Prop [sk-prop-logdet] (logarithm of the Frobenius determinant):
  $\exp\bigl(\sum_{n\ge1}\operatorname{Tr}(F^n\mid V)\,T^n/n\bigr)=\det(1-TF\mid V)^{-1}$
  for any endomorphism $F$ of a finite-dimensional $\overline{\mathbf Q}_\ell$-space.
  Used in §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general],
  §[sec-zeta-weil].

**References.**

- A. Grothendieck et al., *Cohomologie $\ell$-adique et fonctions $L$*
  (SGA 5), Exposé III: trace-class evaluations (4.4.3)–(4.4.7) and
  Theorem 4.4 (Lefschetz–Verdier pushforward compatibility).
- Y. Varshavsky, *Lefschetz–Verdier trace formula and a generalization of a
  theorem of Fujiwara*, GAFA 17 (2007), Def. 2.1.1 and Thm. 2.1.3
  (local terms of contracting correspondences).
- M. Artin, A. Grothendieck, J.-L. Verdier, *Théorie des topos et
  cohomologie étale des schémas* (SGA 4), Exposés XVII–XVIII; P. Deligne,
  *Cohomologie étale* (SGA 4½), Rapport, §3.
- B. Bhatt and P. Scholze, *The pro-étale topology for schemes*,
  Astérisque 369 (2015).
- Stacks Project: `04DF`, `0CCB` (universal homeomorphisms, relative
  Frobenius); `06LH`, `0FMG`, `0B2P` (finite schemes over a field,
  $\mathbf P^1$ proper and smooth of dimension one); `087J`, `03TJ`
  (filtered derived categories, additivity of traces); `09AW` (derived
  limits of perfect complexes).
