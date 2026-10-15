+++
kind = "proof"
of = "sk-lem-sf-mate"
uses = ["sk-thm-sf-comp-composition", "sk-prop-sf-existence"]
+++
(1) For $A\in\Loc(\Dctf(X,\Lambda))$ and $B\in\Loc(\Dctf(Z,\Lambda))$,

$$
\Hom(A,f^!g^!B)\simeq\Hom(Rf_!A,g^!B)\simeq\Hom(Rg_!Rf_!A,B)\simeq\Hom(R(gf)_!A,B),
$$

the last step by [sk-thm-sf-comp-composition]. The Yoneda lemma gives
$f^!g^!\simeq(gf)^!$. Passing to right adjoints transforms the associativity
and identity constraints of [sk-thm-sf-comp-composition] (1) into those for
$f^!$.

(2) For an open immersion, $Rj_!=j_!$ (take the trivial compactification
$p=\mathrm{id}$), and $j_!\dashv j^*$ on the localizing categories. By
uniqueness of right adjoints, $j^!\simeq j^*$.

(3) From $f\circ u=v\circ f_V$ and (1), (2) we get
$u^*f^!\simeq(fu)^!=(vf_V)^!\simeq f_V^!v^*$. Together with
$j^*f^!\simeq(fj)^!$ for an open $j:U\to X$, which is (1) and (2), this gives
the locality statement.

(4) On $\Loc(\Dctf(-,\Lambda))$, $j^*$ is right adjoint to $j_!$ and $p^!$ to
$Rp_*=Rp_!$, so $j^*\circ p^!$ is right adjoint to $Rp_*\circ j_!=Rf_!$, and so
is $f^!$. Uniqueness of right adjoints gives the isomorphism.

The proof uses only adjunctions on $\Loc(\Dctf(-,\Lambda))$.
