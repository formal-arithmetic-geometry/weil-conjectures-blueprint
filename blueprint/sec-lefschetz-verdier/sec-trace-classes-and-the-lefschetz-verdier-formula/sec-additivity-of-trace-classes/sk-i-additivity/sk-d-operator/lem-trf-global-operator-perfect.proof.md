+++
kind  = "proof"
of    = "lem-trf-global-operator-perfect"
+++
By [def-trf-coefficient-conventions] the source and the target of
$T_c(u)$ are $R\Gamma_c(X,K)$, which lies in
$D^b_{\mathrm{fin}}(A)$ by
[prop-trf-compact-support-perfectness], and
$D^b_{\mathrm{fin}}(A)$ of [def-trf-categorical-trace] is a
full subcategory of $D(A)$, so it
suffices to see that the composite of
[def-trf-global-operator] is formed in
$D^b_{\mathrm{fin}}(A)$, i.e. that its intermediate complexes are
compact-support cohomology of finite-Tor constructible complexes in
the sense of [def-weil-finite-tor-amplitude]:
$Lc_2^*K$ is finite-Tor constructible, so
$R\Gamma_c(C,Lc_2^*K)\in D^b_{\mathrm{fin}}(A)$; the identification
$Rc_{2*}\cong Rc_{2!}$ for the proper $c_2$ shows that
$Rc_{2*}Lc_2^*K\cong Rc_{2!}Lc_2^*K$ is finite-Tor constructible as
well, so $R\Gamma_c(X,Rc_{2*}Lc_2^*K)\in D^b_{\mathrm{fin}}(A)$;
finally $Rc_1^!K$ is finite-Tor constructible by item (3) of
[def-weil-exceptional-adjoint-admissibility], as required by the
admissibility of
[def-trf-admissibility], so that $R\Gamma_c(C,Rc_1^!K)$ and,
by the identification
$R\Gamma_c(X,Rc_{1!}Rc_1^!K)\cong R\Gamma_c(C,Rc_1^!K)$ of
[def-trf-global-operator] composed with
[def-compact-support-direct-image-detailed],
$R\Gamma_c(X,Rc_{1!}Rc_1^!K)$ are compact-support cohomology of
finite-Tor constructible complexes. Each of these four complexes is
therefore an object of $D^b_{\mathrm{fin}}(A)$, which is the
assertion.
