+++
kind  = "proof"
of    = "sk-thm-smooth-base-change"
+++
*Negative degrees*: both sides vanish for $q<0$.
*Degree zero*: [sk-prop-deg0] (smooth is flat, of finite
presentation, with geometrically reduced fibres).
*Filtered torsion*: $\mathcal F=\varinjlim_n\mathcal F[n]$
over the integers $n$ invertible on $S$, where $\mathcal F[n]$ is the
$n$-torsion subsheaf; inverse images are left adjoints and
$R^qg_*$, $R^qh_*$ commute with filtered colimits for qcqs $g,h$;
so it suffices to handle sheaves annihilated by a single $n$
invertible on $S$. Such a sheaf is a sheaf of $\Lambda/n\Lambda$-modules, and
the higher direct images and the base-change map of a sheaf of
$\Lambda$-modules are those of its underlying abelian sheaf, hence also those
computed for $\Lambda/n\Lambda$-modules. So it suffices to prove
$\mathrm{BC}(f,\Lambda,q)$ for every $q\ge0$ and every coefficient ring
$\Lambda$ in which some $n$ invertible on $S$ vanishes.
*Reduction to relative dimension one*: the assertion is
étale local on $X$ and $S$; the relative dimension of $f$ is locally
constant, so we may assume it constant, equal to $d$; by [sk-prop-normal-form] one may
assume $X$ and $S$
affine and $X\to S$ factoring as an étale morphism to $\Aaf^d_S$ followed by
the projection; writing $\Aaf^d_S\to \Aaf^{d-1}_S\to\cdots\to\Aaf^1_S\to S$
and using the composition compatibility of the base-change map (and that
étale morphisms satisfy base change trivially), it suffices to prove
the assertion for affine smooth $X\to S$ of relative dimension one
with $X$ affine; $n$ remains invertible on each intermediate base.
*Induction on $q$*: for such $f$, prove by strong induction on $q$ that
$\mathrm{BC}(f,\Lambda,q)$ holds universally. For $q\le0$ this is the
negative-degree and degree-zero cases applied to every base change of $f$
(again smooth). For $q\ge1$, with the statement known universally in all
degrees $<q$, [sk-lem-induction] gives $\mathrm{BC}(f,\Lambda,q)$
universally. Specialising along the identity of $S$ gives
$\mathrm{BC}(f,\Lambda,q)$, and running the filtered colimit back over $n$
finishes the proof.
