+++
id = "det-curve-normalization-constant-sheaf"
kind = "lemma"
title = "The normalization sequence of a constant sheaf"
uses = ["lem-sc-normalization-properties", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-geometric-stalk-conservative", "det-curve-finite-support-acyclic", "lem-sc-base-change-curve"]
+++
Let $k$ be algebraically closed, $C$ a reduced separated scheme of finite
type over $k$ of dimension at most one, with irreducible components
$C_1,\dots,C_m$, and let $a:C^{\mathrm{nor}}=\coprod_iC_i^{\nu}\to C$ be the
disjoint union of the normalizations of the components. Let $M$ be a finite
abelian group and $\eta:\underline M_C\to a_*a^{-1}\underline M_C
=a_*\underline M_{C^{\mathrm{nor}}}$ the unit. Then:

1. $a$ is finite and surjective, $C^{\mathrm{nor}}$ is a finite disjoint
   union of smooth connected curves and copies of $\operatorname{Spec}k$, and
   there is a finite set $Z$ of closed points of $C$ such that $a$ is an
   isomorphism over $C\setminus Z$;
2. at a geometric point $\bar x$ of $C$ with $b=b(\bar x)\geq1$ geometric
   points of $C^{\mathrm{nor}}$ above it, $\eta_{\bar x}$ is the diagonal
   $M\to M^b$; hence $\eta$ is injective, and its cokernel $Q$ is supported
   on $Z$ with $Q_{\bar x}=M^b/\Delta M$;
3. the exact sequence $0\to\underline M_C\to a_*\underline M_{C^{\mathrm{nor}}}\to Q\to0$
   gives isomorphisms $H^q(C,\underline M)\cong H^q(C^{\mathrm{nor}},\underline M)$
   for $q\geq2$ and an exact sequence
   $0\to H^0(C,\underline M)\to H^0(C^{\mathrm{nor}},\underline M)\to
   \bigoplus_{z\in Z}Q_{\bar z}\to H^1(C,\underline M)\to
   H^1(C^{\mathrm{nor}},\underline M)\to0$;
4. for an extension $k\subseteq k'$ of algebraically closed fields,
   $a_{k'}:C^{\mathrm{nor}}_{k'}\to C_{k'}$ is the normalization of the
   reduced curve $C_{k'}$, and the sequence of 3 for $C_{k'}$ is the pullback
   of the one for $C$, with the same cokernel stalks.
