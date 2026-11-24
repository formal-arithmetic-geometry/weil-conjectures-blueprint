+++
id = "prose-07-06"
kind = "hidden"
title = "Change of coefficients (4)"
order = 640
+++
We can now define the comparison map for [$f^!$](@theorem-existence-exceptional-inverse-image). Let $f:X\to Y$ be
separated of finite type and $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)}$. Then
$\href{@theorem-existence-exceptional-inverse-image}{f^!K}\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)}$ by Theorem [theorem-exceptional-inverse-image],
and we let

$$
\beta_{f,K}:(\href{@theorem-existence-exceptional-inverse-image}{f^!K})_{\Lambda'}\longrightarrow \href{@theorem-existence-exceptional-inverse-image}{f^!}(K_{\Lambda'})
\tag{7.1}
$$

be the transpose, under the adjunction $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$ on
[$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda'))$](@definition-localizing-subcategory), of the morphism

$$
\href{@proposition-construction-independence-rf-shriek}{Rf_!}((\href{@theorem-existence-exceptional-inverse-image}{f^!K})_{\Lambda'})
\xrightarrow{\sim}(\href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@theorem-existence-exceptional-inverse-image}{f^!K})_{\Lambda'}
\xrightarrow{(\varepsilon_K)_{\Lambda'}}K_{\Lambda'},
$$

whose first arrow is the inverse of the isomorphism of
Lemma [lemma-change-coefficients-compact-support].

The proof below uses three properties of $\beta$. First, the maps $\beta$
are compatible with composition: under $\href{@theorem-existence-exceptional-inverse-image}{(gf)^!}\simeq \href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@theorem-existence-exceptional-inverse-image}{g^!}$ we have
$\beta_{gf,K}=\href{@theorem-existence-exceptional-inverse-image}{f^!}(\beta_{g,K})\circ\beta_{f,\href{@theorem-existence-exceptional-inverse-image}{g^!K}}$. This holds because the
counit of a composite adjunction is the composite of the counits, and
because the comparison for [$Rf_!$](@proposition-construction-independence-rf-shriek) is compatible with the composition
isomorphisms of
Proposition [proposition-composition-base-change-rf-shriek]; both are
determined by their restrictions to the open subscheme. Second, let
$\Lambda\to\Lambda'\to\Lambda''$ be a composite of two maps of the list.
Then $\beta$ for the composite is $\beta$ for $\Lambda'\to\Lambda''$
composed with the extension of scalars to $\Lambda''$ of $\beta$ for
$\Lambda\to\Lambda'$. Indeed, both are transposes of the composite of the
extended counits and the comparisons for [$Rf_!$](@proposition-construction-independence-rf-shriek). Third, for an open
immersion $u$, under $\href{@theorem-existence-exceptional-inverse-image}{u^!}\simeq u^*$, the map $\beta_{u,K}$ is the
isomorphism of Definition [definition-change-of-coefficients-maps](1).
Both are transposes of the same map under $u_!\dashv u^*$.
