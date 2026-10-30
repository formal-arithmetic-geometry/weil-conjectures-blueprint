+++
kind = "proof"
of = "sk-lem-sf-mate"
uses = ["sk-thm-sf-comp-composition"]
+++
(1) For $M\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ and $N\in\Loc(D^b_{\mathrm{ctf}}(Z,\Lambda))$,

$$
\Hom(M,f^!g^!N)
\simeq\Hom(Rf_!M,g^!N)
\simeq\Hom(Rg_!Rf_!M,N)
\simeq\Hom(R(gf)_!M,N),
$$

where the last step holds by Proposition [sk-thm-sf-comp-composition]. By the
Yoneda lemma, $f^!g^!\simeq(gf)^!$. Passing to right adjoints transforms
the associativity and identity constraints of
Proposition [sk-thm-sf-comp-composition](1) into those for $f^!$.

(2) For an open immersion, $Rj_!=j_!$ (take the trivial compactification
$p=\mathrm{id}$), and $j_!\dashv j^*$ on the localizing categories. By
uniqueness of right adjoints, $j^!\simeq j^*$.

(3) Since $f\circ u=v\circ f_V$, parts (1) and (2) show that
$u^*f^!\simeq(fu)^!=(vf_V)^!\simeq f_V^!v^*$. By (1) and (2) we also have
$j^*f^!\simeq(fj)^!$ for an open $j:U\to X$, and together these give the
locality statement.

(4) On $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$, $j^*$ is right adjoint to $j_!$ and $p^!$
to $Rp_*=Rp_!$. Hence $j^*\circ p^!$ is right adjoint to $Rp_*\circ j_!=Rf_!$,
and so is $f^!$. By uniqueness of right adjoints, the two are isomorphic.
