package com.example.imagens;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    // Views Tela Login
    public Button btn_login;

    // Views Tela Principal
    public Button btn_sobre;
    public Button btn_config;
    public Button btn_sair;

    // Views Tela Sobre App
    public Button tela_sobre_btn_voltar;

    // Views Tela Config
    public Button tela_config_btn_voltar;

    public EditText txt_login;
    public EditText txt_password;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);

        carregaTelaLogin();
    }
    public void carregaTelaLogin(){
        setContentView(R.layout.tela_login);

        btn_login = findViewById(R.id.btn_login);
        txt_login = findViewById(R.id.txt_login);
        txt_password = findViewById(R.id.txt_password);

        btn_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (
                        txt_login.getText().toString().equals("Jovi") &&
                        txt_password.getText().toString().equals("123")
                )
                    carregaTelaPrincipal();
            }
        });
    }

    public void carregaTelaPrincipal(){
        setContentView(R.layout.tela_principal);

        btn_config = findViewById(R.id.btn_config);
        btn_sobre = findViewById(R.id.btn_sobre);
        btn_sair = findViewById(R.id.btn_sair);

        btn_config.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                carregaTelaConfiguracao();
            }
        });

        btn_sobre.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                carregaTelaSobre();
            }
        });

        btn_sair.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                carregaTelaLogin();
            }
        });

    }


    public void carregaTelaConfiguracao(){
        setContentView(R.layout.tela_configuracoes);

        tela_config_btn_voltar = findViewById(R.id.tela_config_btn_voltar);

        tela_config_btn_voltar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                carregaTelaPrincipal();
            }
        });
    }

    public void carregaTelaSobre(){
        setContentView(R.layout.sobre_o_app);

        tela_sobre_btn_voltar = findViewById(R.id.tela_sobre_btn_voltar);

        tela_sobre_btn_voltar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                carregaTelaPrincipal();
            }
        });

    }
}

