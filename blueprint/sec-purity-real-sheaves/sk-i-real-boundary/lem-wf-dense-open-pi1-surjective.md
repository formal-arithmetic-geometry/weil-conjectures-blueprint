+++
id = "lem-wf-dense-open-pi1-surjective"
kind = "lemma"
title = "Fundamental groups of a dense open surject"
order = 2986
uses = ["cor-galois-lisse-representations", "d-real-setup", "def-galois-fibre-functor", "def-weil-pbc-constructible-complexes", "def-wf-fundamental-representation", "def-wf-middle-extension", "def-wf-weil-group", "lem-a1-lisse-middle-extension", "lem-fet-galois-category", "lem-fin-etale-normal-components", "lem-fin-normal-open-lisse-image", "lem-galois-transitive", "lem-wf-weil-group-exact-sequence", "prop-wf-weil-sheaf-representation-equivalence", "thm-galois-fundamental"]
+++
Let $V$ be a connected normal Noetherian scheme, let
$k:V'\hookrightarrow V$ be a dense open immersion, and let $\bar v$ be a
geometric point of $V'$, with the fundamental groups of
[def-galois-fibre-functor].

1. (*Geometric surjectivity.*) The map
   $\pi_1(V',\bar v)\to\pi_1(V,\bar v)$ induced by pullback of finite
   etale covers is surjective. Equivalently, a connected finite etale
   cover of $V$ stays connected over $V'$.
2. (*Weil groups.*) Let $V_0$ be a separated finite-type $k_0$-scheme
   whose base change $V=V_0\times_{k_0}k$ is connected and normal, let
   $V'_0\subseteq V_0$ be a dense open, and put
   $V'=V'_0\times_{k_0}k$. Then the induced map of Weil groups
   $W(V'_0)\to W(V_0)$ of [def-wf-weil-group] commutes with the degree
   maps, restricts on the geometric subgroups to the surjection of (1),
   and is surjective.
3. (*Lisse sheaves extend uniquely.*) For every lisse sheaf
   $\mathcal N$ on $V$ (at every finite coefficient level, hence for
   lisse $\Qlb$-sheaves in the convention of
   [def-weil-pbc-constructible-complexes]) the adjunction unit
   $\mathcal N\to k_*k^*\mathcal N$ is an isomorphism.
4. (*Restriction on curves.*) Let $U_0$ be a curve in the sense of
   [d-real-setup] and $k:U'_0\hookrightarrow U_0$ a nonempty open.
   Pullback $k^*$ from lisse Weil sheaves on $U_0$ to lisse Weil sheaves
   on $U'_0$ is fully faithful, and it carries irreducible objects (no
   lisse subsheaf other than $0$ and itself) to irreducible objects. The
   same holds for lisse $\Qlb$-sheaves on the geometric curves
   $U'\hookrightarrow U$.
5. (*Constructibility.*) If $j:U_0\hookrightarrow C_0$ is a nonempty
   open in a curve $C_0$ of [d-real-setup] and $\mathcal F$ is lisse on
   $U_0$, then the middle extension $j_*\mathcal F$ of
   [def-wf-middle-extension] is constructible at every finite
   coefficient level.
