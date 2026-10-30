+++
kind = "proof"
of = "sk-thm-pe-classical-sheaves"
uses = ["det-pe-classical-sheaves-unit", "det-pe-classical-sheaves-modules", "sk-prop-pe-comparison-morphism", "sk-prop-pe-affine-basis"]
+++
Evaluating on étale objects, we see that
$F\xrightarrow{\sim}\nu_{X,*}\nu_X^*F$, which proves full
faithfulness. Moreover,
every $\nu_X^*F$ is classical by (2.6).
Conversely, let $G$ be classical. On a pro-étale affine the counit
$\nu_X^*\nu_{X,*}G\to G$ is

$$
(\nu_X^*\nu_{X,*}G)(U)
=\varinjlim_iG(U_i)\longrightarrow G(U),
$$

which is an isomorphism by (2.4). Since
pro-étale affines form a covering basis
(Proposition [sk-prop-pe-affine-basis]), the counit is an
isomorphism of sheaves.
