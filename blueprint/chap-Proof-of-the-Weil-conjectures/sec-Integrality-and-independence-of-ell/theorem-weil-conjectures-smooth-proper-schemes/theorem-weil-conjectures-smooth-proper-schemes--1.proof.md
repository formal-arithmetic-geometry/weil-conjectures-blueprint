+++
kind = "proof"
of = "theorem-weil-conjectures-smooth-proper-schemes--1"
order = 1391003
+++
For odd $i$, let $R_i$ be the submultiset of the reciprocal roots of $A$
whose absolute value under every complex embedding is $q^{i/2}$, and
for even $i$ define $R_i$ in the same way using the reciprocal roots of
$B$. By Lemma [lemma-reciprocal-roots-zeta], every reciprocal root
of $A$ or $B$ lies in exactly one $R_i$. The multisets of reciprocal
roots of $A$ and $B$ are Galois-stable, with multiplicities. The
condition on all complex embeddings is Galois-invariant, and so each
$R_i$ is Galois-stable. Put

$$
P_i(T)=\prod_{a\in R_i}(1-aT).
$$

The coefficients of $P_i$ are integers, being rational by Galois
invariance and algebraic integers because the roots satisfy monic
integral equations.

Now let $\ell\nmid q$ be any prime and
$\theta:\overline{\mathbf Q}\hookrightarrow\overline{\mathbf Q}_\ell$ an embedding. By
(19.2) and
Lemma [lemma-reciprocal-roots-zeta], the embedding $\theta$ maps
$R_i$ onto the multiset of Frobenius eigenvalues on $H^i_\ell$. Since
both polynomials have constant coefficient one, $P_i=P_{i,\ell}$ in
$\overline{\mathbf Q}_\ell[T]$, hence in $\mathbf Q_\ell[T]$. As $\ell$ was arbitrary,
this proves the existence in (1).

*Source:* the proof of Theorem [theorem-weil-conjectures-smooth-proper-schemes].
