+++
id = "thm-sc-open-uniform-cd"
kind = "theorem"
title = "A uniform bound for direct image by an open immersion"
order = 1582
uses = ["def-sc-etale-torsion-cd", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-sc-cech-spectral", "lemma-weil-pbc-etale-cohomology-continuity", "prop-weil-pbc-strict-henselization-stalk-formula", "thm-sc-affine-torsion-cd"]
+++
Let $T$ be a finite-type scheme over $K$, with
$\operatorname{cd}_{\rm tor}(K)\leq c$, and let
$j:U\hookrightarrow T$ be a
quasi-compact open immersion,
Choose a finite affine cover $T=\bigcup_\alpha T_\alpha$.
Cover $U\cap T_\alpha$ by $r_\alpha\geq1$ principal opens
of $T_\alpha$, allowing an empty principal open if necessary.
Put $D=\dim T$ and

$$
N=D+c+\max_\alpha(r_\alpha-1).
$$

For every torsion etale sheaf
$M$ on $U$, the
higher direct images
satisfy $R^qj_*M=0$ for $q>N$.
The field bound is the one of [def-sc-etale-torsion-cd].

## Proof

Fix a geometric point of $T_\alpha$. Its affine pointed
etale neighborhoods $V\to T_\alpha$ form a cofinal system.
They have dimension at most $D$ and are finite type over $K$.
The chosen principal opens pull back to a cover of $U\times_TV$;
each finite intersection is again principal open in $V$, hence
affine of dimension at most $D$.
By [thm-sc-affine-torsion-cd], its cohomology with any
restricted torsion sheaf vanishes above $D+c$.
The alternating finite-cover Cech spectral sequence of
[lem-sc-cech-spectral] has cover degree
$0\leq p\leq r_\alpha-1$. Its total degrees are therefore
at most $D+c+r_\alpha-1\leq N$.
Take the filtered colimit over $V$. By
[lemma-weil-pbc-etale-cohomology-continuity], [prop-weil-pbc-strict-henselization-stalk-formula]
this colimit is the geometric stalk of $R^qj_*M$.
It is zero for $q>N$, uniformly in the point and in $M$.
All stalks vanish, so the sheaf is zero.
