+++
id = "lemma-kunneth-formula-compact-supports--3"
kind = "lemma"
title = "Projection formula for compact supports"
order = 1225005
aliases = ["bp-r377-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleExceptionalProjectionMorphism"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be a prime,
and let $E$ be a field that is an admissible coefficient ring, for instance $\overline{\mathbf Q}_\ell$. Let $a:U\to V$ be a morphism of
separated schemes of finite type over $k$. For bounded constructible
$E$-complexes $A$ on $U$ and $B$ on $V$, the exceptional projection map

$$
Ra_!A\otimes B\longrightarrow Ra_!(A\otimes a^*B)
$$

is an isomorphism. Taking $a=f$, $A=K$ and $B=Rg_!L$, its inverse gives

$$
Rf_!(K\otimes f^*Rg_!L)\simeq Rf_!K\otimes Rg_!L.
$$

Taking $a=p_1$, $A=p_2^*L$ and $B=K$ instead, and using the symmetry
of the tensor product, gives

$$
Rp_{1!}(p_1^*K\otimes p_2^*L)\simeq K\otimes Rp_{1!}p_2^*L.
$$

The composite

$$
Rh_!(p_1^*K\otimes p_2^*L)
\simeq Rf_!(K\otimes Rp_{1!}p_2^*L)
\simeq Rf_!(K\otimes f^*Rg_!L)
\simeq Rf_!K\otimes Rg_!L
$$

of the projection formula for $p_1$, the base change isomorphism of
[lemma-kunneth-formula-compact-supports--2] and the projection formula
for $f$ is called the *Künneth isomorphism*
$Rh_!(K\boxtimes_SL)\simeq Rf_!K\otimes Rg_!L$.
