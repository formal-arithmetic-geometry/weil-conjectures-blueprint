+++
id = "prose-07-06"
kind = "hidden"
title = "Change of coefficients (4)"
order = 640
+++
We can now define the comparison map for $f^!$. Let $f:X\to Y$ be
separated of finite type and $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. Then
$f^!K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ by Theorem [theorem-exceptional-inverse-image],
and we let

$$
\beta_{f,K}:(f^!K)_{\Lambda'}\longrightarrow f^!(K_{\Lambda'})
\tag{7.1}
$$

be the transpose, under the adjunction $Rf_!\dashv f^!$ on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda'))$, of the morphism

$$
Rf_!((f^!K)_{\Lambda'})
\xrightarrow{\sim}(Rf_!f^!K)_{\Lambda'}
\xrightarrow{(\varepsilon_K)_{\Lambda'}}K_{\Lambda'},
$$

whose first arrow is the inverse of the isomorphism of
Lemma [lemma-change-coefficients-compact-support].

The proof below uses three properties of $\beta$. First, the maps $\beta$
are compatible with composition: under $(gf)^!\simeq f^!g^!$ we have
$\beta_{gf,K}=f^!(\beta_{g,K})\circ\beta_{f,g^!K}$. This holds because the
counit of a composite adjunction is the composite of the counits, and
because the comparison for $Rf_!$ is compatible with the composition
isomorphisms of
Proposition [proposition-composition-base-change-rf-shriek]; both are
determined by their restrictions to the open subscheme. Second, let
$\Lambda\to\Lambda'\to\Lambda''$ be a composite of two maps of the list.
Then $\beta$ for the composite is $\beta$ for $\Lambda'\to\Lambda''$
composed with the extension of scalars to $\Lambda''$ of $\beta$ for
$\Lambda\to\Lambda'$. Indeed, both are transposes of the composite of the
extended counits and the comparisons for $Rf_!$. Third, for an open
immersion $u$, under $u^!\simeq u^*$, the map $\beta_{u,K}$ is the
isomorphism of Definition [definition-change-of-coefficients-maps](1).
Both are transposes of the same map under $u_!\dashv u^*$.
