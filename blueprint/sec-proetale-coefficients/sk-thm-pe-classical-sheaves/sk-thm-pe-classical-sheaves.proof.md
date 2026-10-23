+++
kind = "proof"
of = "sk-thm-pe-classical-sheaves"
uses = ["det-pe-classical-sheaves-unit", "det-pe-classical-sheaves-modules", "sk-prop-pe-comparison-morphism", "sk-prop-pe-affine-basis"]
+++
Evaluation on étale objects gives $F\xrightarrow{\sim}\nu_{X,*}\nu_X^*F$ in
$\Sh(X_{\Et})$, hence full faithfulness ([det-pe-classical-sheaves-unit]), and
every $\nu_X^*F$ is classical by the affine evaluation formula of
[sk-prop-pe-comparison-morphism]. Conversely, let $G$ be classical. On a
pro-étale affine the counit $\nu_X^*\nu_{X,*}G\to G$ of sheaves on $X_{\Proet}$
is

$$
(\nu_X^*\nu_{X,*}G)(U)=\varinjlim_iG(U_i)\longrightarrow G(U),
$$

which is an isomorphism because $G$ is classical. Since pro-étale affines form a
covering basis ([sk-prop-pe-affine-basis]), the counit is an isomorphism of sheaves. The module statement follows because
$\nu_X^*$ is exact and both adjoint functors preserve module structures
([det-pe-classical-sheaves-modules]).
