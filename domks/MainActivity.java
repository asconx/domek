package com.example.domeklol;

import android.os.Bundle;
import com.google.android.material.snackbar.Snackbar;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;
import com.example.domeklol.databinding.ActivityMainBinding;

import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    int likes = 0;
    TextView likesCounter;


    private AppBarConfiguration appBarConfiguration;
private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        likesCounter = findViewById(R.id.buttonlike);





    }
    private void refreshLikeCounter(){likesCounter.setText(likes + "polubien");}

    public void onClickBtnLike(View view){
        likes++;
        refreshLikeCounter();
    }
    public void onClickBtnDelete(View view){
        likes--;
        if(likes<0){
            likes=0;
        }
    }

}