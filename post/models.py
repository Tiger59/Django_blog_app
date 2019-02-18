"""モジュールインポート"""
import uuid

from django.db import models
"""Djangoには標準のユーザー認証モデルが付属している"""
from django.contrib.auth.models import User


"""モデルクラス定義"""
class Post(models.Model):
    """フィールド定義"""
    # IntegerField: 整数
    # primary_key: プライマリーキー
    id = models.IntegerField(primary_key=True)
    # default: 指定された関数が自動で実行されて、返ってきた値を入れる
    # editable: モデルから変更できないようにロックをかける
    post_id = models.UUIDField(default=uuid.uuid4, editable=False)
    # CharField: 文字列
    # max_length: 最大長
    title = models.CharField(max_length=150, unique=True)
    # ForeignKey: 外部キー、参照するテーブル定義モデルを指定
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # TextField: 長文テキスト
    content = models.TextField()
    # DateTimeField: pythonのdatetimeクラスをベースとした日時
    # auto_now_add: データ作成時に自動で現在時刻を挿入する
    published_at = models.DateTimeField(auto_now_add=True)
    # ImageField: 画像フォルダーに追加される
    image = models.ImageField(upload_to='images/')
    # auto_now: 変更時に現在時刻を挿入する
    # updated_at = models.DateTimeField(auto_now=True)

    """テーブル名やインデックスなどの定義"""
    class Meta:
        # SQLテーブル名
        db_table = 'post'
        # 例: 管理画面で使用するモデル名称
        verbose_name = 'Post/記事'
        verbose_name_plural = 'Posts/記事'
        # インデックス定義
        indexes = [
            models.Index(fields=['post_id']),
            models.Index(fields=['author']),
            models.Index(fields=['published_at']),
        ]


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag/タグ'
        verbose_name_plural = 'Tags/タグ'
        indexes = [
            models.Index(fields=['tag_id']),
            models.Index(fields=['name']),
        ]


class Tagging(models.Model):
    id = models.IntegerField(primary_key=True)
    tagging_id = models.UUIDField(default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tagging'
        verbose_name = 'Tagging/記事タグ関連'
        verbose_name_plural = 'Taggings/記事タグ関連'
        indexes = [
            models.Index(fields=['tagging_id']),
            models.Index(fields=['post']),
            models.Index(fields=['tag']),
        ]