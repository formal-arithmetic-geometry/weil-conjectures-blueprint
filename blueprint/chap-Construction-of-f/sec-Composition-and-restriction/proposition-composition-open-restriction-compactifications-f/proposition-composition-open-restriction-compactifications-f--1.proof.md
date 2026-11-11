+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f--1"
order = 530003
uses = ["proposition-composition-base-change-rf-shriek--1", "proposition-sp-unique-adjoint--1"]
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

*Source:* the proof of Proposition [proposition-composition-open-restriction-compactifications-f].
