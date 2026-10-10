+++
kind  = "proof"
of    = "thm-sf-fullcd-etale-origin"
+++
The morphism $p$ is proper and of finite type, in particular quasi-compact
and quasi-separated, and $\mathcal G$ lies in
$D^+(\overline X_{\Et},A)$, so the comparison direct image of
[prop-weil-pbc-comparison-direct-image] gives

$$
Rp_*\nu_{\overline X}^*\mathcal G\cong\nu_Y^*Rp_{\Et,*}\mathcal G .
$$

By [lem-sf-etale-direct-image-vanishing] the higher direct images of
$p$ on the étale sites vanish above $2d$ for *every* sheaf of
$A$-modules, because $k$ is algebraically closed and
$\dim\overline X\leq d$; that lemma needs no separatedness and no
properness. Hence $\mathcal H^r(Rp_*\mathcal F)=0$ for $r>2d$, which is
the absolute clause of [def-weil-full-cohomological-dimension].
For a base change $V\to Y$ whose source has dimension at most $d$, the
object $V$ of $Y_{\Proet}$ is a weakly étale $Y$-scheme, hence a
scheme, and $p_V:\overline X\times_YV\to V$ is again proper of finite type;
moreover the restriction of $\mathcal F$ to $\overline X\times_YV$ is
the pullback of the étale sheaf
$\mathcal G|_{\overline X\times_YV}$ along the comparison morphism of
$\overline X\times_YV$, by the compatibility of the comparison pullback
with scheme pullback, [lem-weil-pbc-comparison-pullback]. The same
computation therefore applies to $p_V$, with the same bound $2d$, which
is the relative clause.
