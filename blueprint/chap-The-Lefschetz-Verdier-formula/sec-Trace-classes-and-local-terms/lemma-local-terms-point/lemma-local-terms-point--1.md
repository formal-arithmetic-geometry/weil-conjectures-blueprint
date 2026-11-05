+++
id = "lemma-local-terms-point--1"
kind = "lemma"
title = "The pairing and zigzag identity on the point"
name_showing = false
order = 918001
aliases = ["bp-r278-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.integral_traceClass_ofEnd_eq", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointCoev_zigzag"]
uses = ["definition-correspondence", "definition-verdier-dual-evaluation", "lemma-external-duality-trace-morphism", "definition-trace-class-local-terms"]
+++
For this lemma let $k$ be a field of characteristic $p>0$, let $\ell\ne p$
be prime, and put $s=\operatorname{Spec}k$ and
$\Lambda=\overline{\mathbf Q}_\ell$, with its condensed coefficient ring.
Let $K\in\Dbc(s,\Lambda)$ and $u:K\to K$, and put $D=\mathbb D_sK$.
The identity correspondence has fixed locus $s$. Write

$$
\sigma_u:\Lambda_s\longrightarrow K\otimes^{\mathbf L}D,
\qquad
e_u:K\otimes^{\mathbf L}D\longrightarrow\Lambda_s
$$

for the maps in its trace-class construction
(`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointCoev` and
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointPairing`).
Here $\sigma_u$ comes from the class of $1_K$ under inverse external
duality, pullback to the diagonal, and adjunction along the fixed locus;
$e_u$ comes from evaluation and the identification $\omega_s\simeq\Lambda_s$.
Then

$$
\int_s\operatorname{Tr}_{\mathrm{id}}(u)
=e_u\circ(u\otimes^{\mathbf L}1_D)\circ\sigma_u.
$$

Moreover, with the associativity and unit isomorphisms understood,

$$
(1_K\otimes^{\mathbf L}e_u)\circ
(\beta_{K,K}\otimes^{\mathbf L}1_D)\circ
(1_K\otimes^{\mathbf L}\sigma_u)=1_K,
$$

where $\beta$ is the Koszul symmetry. These two identities do not require
a chosen right dual of $K$.
