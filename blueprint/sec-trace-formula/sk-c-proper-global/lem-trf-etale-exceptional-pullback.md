+++
id = "lem-trf-etale-exceptional-pullback"
kind = "lemma"
title = "Exceptional pullback along an etale morphism"
order = 2472
uses = ["def-pur-smooth-purity-map", "def-sbc-smooth-morphisms", "def-trf-admissibility", "def-trf-etale-base-change", "def-weil-exceptional-inverse-image", "def-weil-scheme-morphism-properties", "prop-functor-package", "thm-pur-cohomological-smoothness"]
+++
In the situation of [def-trf-etale-base-change], with $c_1$
and $c_1'$ exceptionally admissible,
the canonical comparison

$$
Le_C^*Rc_1^!K\xrightarrow{\ \sim\ }Rc_1'^!Le^*K
$$

is an isomorphism.

## Proof

The schemes $X,X'$ are separated of finite type over $k$ by the
standing conventions of [def-trf-admissibility], so the etale
morphism $e:X'\to X$ is separated; being etale it is also smooth of
pure relative dimension $0$ ([def-weil-scheme-morphism-properties],
[def-sbc-smooth-morphisms]), and its base change
$e_C:C'\to C$ is etale, hence smooth of pure relative dimension
$0$, as well.
By the smooth purity map [def-pur-smooth-purity-map] in relative
dimension $0$ and the tensor formula of
[thm-pur-cohomological-smoothness], the canonical comparison
$Le^*\to Re^!$ is an isomorphism on $D^b_{ctf}(X,A)$ (the twist
$\Lambda(0)[0]$ is trivial), and likewise $Le_C^*\to Re_C^!$ on
$D^b_{ctf}(C,A)$.
The composition isomorphisms for the exceptional inverse image, which
are part of the six-operations package
([prop-functor-package] and
[def-weil-exceptional-inverse-image]), give
$R(c_1e_C)^!\cong Re_C^!Rc_1^!$ and
$R(ec_1')^!\cong Re^!Rc_1'^!$, and the commutativity of the
base-change square gives $c_1e_C=ec_1'$. Composing these canonical
identifications,

$$
Le_C^*Rc_1^!K\xrightarrow{\ \sim\ }Re_C^!Rc_1^!K
\xrightarrow{\ \sim\ }R(c_1e_C)^!K=R(ec_1')^!K
\xrightarrow{\ \sim\ }Re^!Rc_1'^!K
\xrightarrow{\ \sim\ }Le^*Rc_1'^!K,
$$

exhibits the canonical comparison $Le_C^*Rc_1^!K\to Rc_1'^!Le^*K$
as a composite of isomorphisms, hence as an isomorphism. (The smooth
purity map is a statement of the smooth-purity chapter of this
manuscript, placed after the present chapter; [thm-weil-six-operations] quotes the same theorem in the six-operations interface, so no new input is
introduced.)
