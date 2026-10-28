+++
kind  = "proof"
of    = "lem-sf-fullcd-detection-equivalence"
+++
*Auxiliary fact.* Let $T$ be a scheme, let $W\to T$ be an object of
$T_{\Proet}$ every pro-étale covering family of which contains a member
admitting a section – a weakly contractible object, the objects whose
existence in abundance is Stacks Project, Pro-étale Cohomology, Lemma
61.13.4, [Tag 0990](https://stacks.math.columbia.edu/tag/0990), and
which are the ones used in [lem-sf-proetale-vanishing-detection]. Then
$H^q(W,\mathcal G)=0$ for every $q>0$ and every sheaf $\mathcal G$ of
$A$-modules on $T_{\Proet}$: the functor
$\mathcal G\mapsto\mathcal G(W)$ is left exact, and it is right exact
because for a surjection $\mathcal G\to\mathcal G'$ and a section of
$\mathcal G'$ over $W$ there is a covering family of $W$ on which the
section lifts, and one of its members admits a section $W\to W_i$ along
which the lift pulls back. Hence the global-sections functor of the site
over $W$ is exact and its higher derived functors vanish.

*The Leray identification.* Fix an object $V\to Y$ of $Y_{\Proet}$, a sheaf
$\mathcal F$ of $A$-modules on $\overline X_{\Proet}$, and put
$\mathcal Q^r=\mathcal H^r(R(p_V)_*(\mathcal F|_{\overline X\times_YV}))$
([def-weil-derived-cohomology-sheaves]). For an object $W\to V$ of
$V_{\Proet}$ the sections of $(p_V)_*\mathcal G$ over $W$ are the sections of
$\mathcal G$ over $\overline X\times_VW=\overline X\times_YW$, so
$\Gamma\bigl((\overline X\times_YW)_{\Proet},-\bigr)=\Gamma\bigl(W,-\bigr)\circ(p_V)_*$
on sheaves on $(\overline X\times_YV)_{\Proet}$, and the Leray spectral
sequence of this composite, which exists by [thm-sp-grothendieck], has
$E_2^{p,q}=H^p\bigl(W,\mathcal Q^q\bigr)$. If $W$ is weakly contractible,
the auxiliary fact (with $T=V$) kills the terms with $p>0$, so the spectral
sequence collapses at $p=0$:

$$
H^r\bigl((\overline X\times_YW)_{\Proet},\mathcal F|_{\overline X\times_YW}\bigr)
\cong\mathcal Q^r(W).
$$

For a general object $W$ the terms with $p>0$ survive, which is why the
statement only tests weakly contractible $W$ (for $p=\mathrm{id}_Y$ and
$W=V$ the left side is $H^r(V_{\Proet},\mathcal F|_V)$ while $\mathcal Q^r=0$
for $r>0$).

*The condition implies the vanishing.* Assume
$\operatorname{FullCD}(p,A;c)$. By its relative clause $\mathcal Q^r=0$ for
$r>c$, so by the identification
$H^r\bigl((\overline X\times_YW)_{\Proet},\mathcal F|_{\overline X\times_YW}\bigr)=\mathcal Q^r(W)=0$
for $r>c$ and every affine weakly contractible $W\to V$.
*The vanishing implies the condition.* Assume the vanishing of the
statement and fix $V\to Y$ and $\mathcal F$. For every affine weakly
contractible object $W\to V$ of $V_{\Proet}$ the identification gives
$\mathcal Q^r(W)=0$ for $r>c$. The affine weakly
contractible objects of $V_{\Proet}$ detect the vanishing of a sheaf by
[lem-sf-proetale-vanishing-detection](i), so $\mathcal Q^r=0$ for
$r>c$. As $V$ was arbitrary this is the relative clause of
$\operatorname{FullCD}(p,A;c)$, and $V=Y$ gives the absolute clause; this is
also the form of the test recorded in
[cor-sf-fullcd-weakly-contractible-test].
