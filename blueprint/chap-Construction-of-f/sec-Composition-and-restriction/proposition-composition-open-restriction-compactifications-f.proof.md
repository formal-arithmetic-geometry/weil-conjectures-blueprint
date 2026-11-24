+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f"
order = 531
uses = ["proposition-composition-base-change-rf-shriek", "proposition-sp-unique-adjoint"]
+++
Each statement is the right adjoint of a statement about lower shriek
functors already proved, and we conclude by uniqueness of adjoints.

(1) For $M\in\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)})$ and $N\in\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Z,\Lambda)})$,

$$
\Hom(M,\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@theorem-existence-exceptional-inverse-image}{g^!N})
\simeq\Hom(\href{@proposition-construction-independence-rf-shriek}{Rf_!M},\href{@theorem-existence-exceptional-inverse-image}{g^!N})
\simeq\Hom(\href{@proposition-construction-independence-rf-shriek}{Rg_!}\href{@proposition-construction-independence-rf-shriek}{Rf_!M},N)
\simeq\Hom(\href{@proposition-construction-independence-rf-shriek}{R(gf)_!M},N),
$$

where the last step holds by Proposition [proposition-composition-base-change-rf-shriek]. By the
Yoneda lemma, $\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@theorem-existence-exceptional-inverse-image}{g^!}\simeq\href{@theorem-existence-exceptional-inverse-image}{(gf)^!}$. Passing to right adjoints transforms
the associativity and identity constraints of
Proposition [proposition-composition-base-change-rf-shriek](1) into those for [$f^!$](@theorem-existence-exceptional-inverse-image).

(2) For an open immersion, $\href{@proposition-construction-independence-rf-shriek}{Rj_!}=j_!$ (take the trivial compactification
$p=\mathrm{id}$), and $j_!\dashv j^*$ on the [localizing categories](@definition-localizing-subcategory); here
we use that $j^*$ preserves the [localizing categories](@definition-localizing-subcategory), as inverse images
do (see the proof of Proposition [proposition-proper-base-change-localizing-categories]). By
uniqueness of right adjoints, $\href{@theorem-existence-exceptional-inverse-image}{j^!}\simeq j^*$.

(3) Since $f\circ u=v\circ f_V$, parts (1) and (2) show that
$u^*\href{@theorem-existence-exceptional-inverse-image}{f^!}\simeq\href{@theorem-existence-exceptional-inverse-image}{(fu)^!}=\href{@theorem-existence-exceptional-inverse-image}{(vf_V)^!}\simeq \href{@theorem-existence-exceptional-inverse-image}{f_V^!}v^*$. For an open $j:U\to X$,
parts (1) and (2) also give $j^*\href{@theorem-existence-exceptional-inverse-image}{f^!}\simeq\href{@theorem-existence-exceptional-inverse-image}{(fj)^!}$. These two isomorphisms
show that [$f^!$](@theorem-existence-exceptional-inverse-image) is local on $X$ and on $Y$.

(4) On [$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$](@definition-localizing-subcategory), $j^*$ is right adjoint to $j_!$ and [$p^!$](@theorem-existence-exceptional-inverse-image)
to $Rp_*=\href{@proposition-construction-independence-rf-shriek}{Rp_!}$, so $j^*\circ \href{@theorem-existence-exceptional-inverse-image}{p^!}$ and [$f^!$](@theorem-existence-exceptional-inverse-image) are both right adjoint to
$Rp_*\circ j_!=\href{@proposition-construction-independence-rf-shriek}{Rf_!}$, and they are isomorphic by uniqueness of right adjoints.
