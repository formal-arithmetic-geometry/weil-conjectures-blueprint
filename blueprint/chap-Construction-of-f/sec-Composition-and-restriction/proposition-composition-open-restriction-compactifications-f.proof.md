+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f"
order = 531
uses = ["proposition-composition-base-change-rf-shriek", "proposition-sp-unique-adjoint"]
+++
Each statement is the right adjoint of a statement about lower shriek
functors already proved, and we conclude by uniqueness of adjoints.

(1) For $M\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ and $N\in\Loc(D^b_{\mathrm{ctf}}(Z,\Lambda))$,

$$
\Hom(M,f^!g^!N)
\simeq\Hom(Rf_!M,g^!N)
\simeq\Hom(Rg_!Rf_!M,N)
\simeq\Hom(R(gf)_!M,N),
$$

where the last step holds by Proposition [proposition-composition-base-change-rf-shriek]. By the
Yoneda lemma, $f^!g^!\simeq(gf)^!$. Passing to right adjoints transforms
the associativity and identity constraints of
Proposition [proposition-composition-base-change-rf-shriek](1) into those for $f^!$.

(2) For an open immersion, $Rj_!=j_!$ (take the trivial compactification
$p=\mathrm{id}$), and $j_!\dashv j^*$ on the localizing categories; here
we use that $j^*$ preserves the localizing categories, as inverse images
do (see the proof of Proposition [proposition-proper-base-change-localizing-categories]). By
uniqueness of right adjoints, $j^!\simeq j^*$.

(3) Since $f\circ u=v\circ f_V$, parts (1) and (2) show that
$u^*f^!\simeq(fu)^!=(vf_V)^!\simeq f_V^!v^*$. For an open $j:U\to X$,
parts (1) and (2) also give $j^*f^!\simeq(fj)^!$. These two isomorphisms
show that $f^!$ is local on $X$ and on $Y$.

(4) On $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$, $j^*$ is right adjoint to $j_!$ and $p^!$
to $Rp_*=Rp_!$, so $j^*\circ p^!$ and $f^!$ are both right adjoint to
$Rp_*\circ j_!=Rf_!$, and they are isomorphic by uniqueness of right adjoints.
