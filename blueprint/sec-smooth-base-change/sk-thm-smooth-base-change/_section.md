+++
id = "sk-thm-smooth-base-change"
kind = "section"
title = "Smooth base change"
order = 1416
uses = ["sk-def-bc", "sk-def-smooth", "sk-lem-induction", "sk-prop-deg0", "sk-prop-input-spreading", "sk-prop-input-torsors"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_smooth"]
+++
*Theorem (sketch).*

Let

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y\\
f\downarrow & & \downarrow e\\
S & \xleftarrow{\;g\;} & T
\end{array}
$$

be Cartesian with $f$ smooth and $g$ quasi-compact
quasi-separated, and let $\Lambda$ be a commutative ring. Then for
every $q$ and every sheaf $\mathcal F$ of $\Lambda$-modules on $T_{\Et}$
all of whose geometric stalks are torsion of orders invertible on $S$
(each element killed by a positive integer invertible on $S$),

$$
f^{-1}R^qg_*\mathcal F\ \xrightarrow{\ \sim\ }\ R^qh_*e^{-1}\mathcal F,
$$

the map being the base-change map of [sk-def-bc].

## Proof

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
